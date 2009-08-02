# Copyright 2009 Lee Harr
#
# This file is part of pybotwar.
#
# Pybotwar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pybotwar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pybotwar.  If not, see <http://www.gnu.org/licenses/>.


import subprocess
from subprocess import PIPE
import time

import world
from world import box2d


def run(testmode=False):
    python = '/usr/bin/python'
    ctrlpy = 'control.py'
    r1 = 'robot01'
    r2 = 'robot02'
    r3 = 'robot03'
    r4 = 'robot04'
    r5 = 'robot05'

    maxforce = 5
    maxtorque = 15

    robots = [r1, r2, r3, r4, r5]
    #robots = [r1]
    #robots = [r1, r1, r1, r1]
    #robots = [r1, r1, r1, r1, r1, r1, r1, r1, r1]
    #robots = [r1, r3, r1, r3, r2, r1, r2, r4, r4]
    #robots = [r1, r3, r1, r3, r1, r4, r4]
    #robots = [r3, r3, r3, r3]
    #robots = [r2]
    #robots = [r2, r2, r2, r2]
    #robots = [r3]
    #robots = [r4]
    #robots = [r4, r4, r4, r4, r4]
    #robots = [r4, r4]
    #robots = [r5]
    #robots = [r5, r5, r5, r5, r5]
    #robots = [r1, r3]
    models = {}
    procs = {}
    results = {}
    timeouts = {}

    w = world.World()
    cl = world.CL()
    w.w.SetContactListener(cl)
    cl.w = w

    for robot in robots:
        robotname = robot
        while robotname in w.robots:
            robotname += '_'
        print 'STARTING', robotname,
        proc = subprocess.Popen([python, ctrlpy, robot, robotname], stdin=PIPE, stdout=PIPE)
        result = proc.stdout.readline().strip()

        if result in ['ERROR', 'END']:
            print 'ERROR!'
        else:
            print 'STARTED'
            model = w.makerobot(robotname)
            models[robotname] = model
            procs[robotname] = proc
            timeouts[robotname] = 0


    t0 = int(time.time())

    result = ''
    rnd = 0
    while (testmode or len(procs) > 1) and not w.v.quit:
        for robotname, model in models.items():
            if robotname not in procs:
                continue

            body = model.body
            pos = body.position
            tur = model.get_turretangle()
            ping = '%s;%s;%s' % (model._pingtype,
                                    model._pingangle,
                                    model._pingdist)
            line = 'TICK:%s|POS:%s|TUR:%s|PING:%s\n' % (rnd, pos, tur, ping)
            #print robotname, line

            proc = procs[robotname]
            proc.stdin.write(line)
            result = proc.stdout.readline().strip()

            if not model.alive:
                del procs[robotname]
                print 'DEAD robot', robotname, 'health is 0'
                proc.kill()
                continue

            if result == 'TIMEOUT':
                timeouts[robotname] += 1
                if timeouts[robotname] > 5:
                    del procs[robotname]
                    print 'REMOVED robot', robotname, 'due to excessive timeouts'
                    proc.kill()

            elif result == 'END':
                del procs[robotname]
                print 'FINISHED: robot', robotname
                proc.kill()

            elif result == 'ERROR':
                del procs[robotname]
                print 'ERROR: robot', robotname
                proc.kill()

            else:
                timeouts[robotname] = 0


            #print 'RR', result, 'RR'
            commands = {}
            try:
                props = result.split('|')
                for prop in props:
                    kind, val = prop.split(':')
                    try:
                        vconv = int(val)
                    except ValueError:
                        pass
                    else:
                        val = vconv
                    commands[kind] = val
            except ValueError:
                continue

            #print 'KV', kind, val
            #print 'R', robot, 'R', result, 'R'
            #print 'R', robotname, 'T', '%s -> %.3f' % (model._turretangletarget, model.turretjoint.GetJointAngle())

            for kind, val in commands.items():
                if kind == 'FORCE':
                    force = maxforce * val/100.0
                    localforce = box2d.b2Vec2(val, 0)
                    worldforce = body.GetWorldVector(localforce)
                    body.ApplyForce(worldforce, pos)
                elif kind == 'TORQUE':
                    torque = maxtorque * val/100.0
                    body.ApplyTorque(torque)
                elif kind == 'FIRE':
                    if val:
                        w.makebullet(robotname)
                elif kind == 'PING':
                    if val:
                        kind, angle, dist = w.makeping(robotname)
                        if kind is not None:
                            model._pingtype = kind[0]
                            model._pingangle = angle
                            model._pingdist = int(dist)
                elif kind == 'TURRET':
                    model.set_turretangle(val)


        w.step()

        rnd += 1
        if not rnd%60:
            print '%s seconds (%s real)' % (rnd/60, int(time.time())-t0)

    print 'FINISHING'

    for robotname, model in models.items():
        if robotname not in procs:
            continue

        line = 'FINISH\n'
        proc = procs[robotname]
        proc.stdin.write(line)

    alive = [model for model in models.values() if model.alive]

    if not testmode and len(alive)==1:
        print 'WINNER:', alive[0].name



if __name__ == '__main__':
    import sys
    testmode = False
    if len(sys.argv) > 1:
        if sys.argv[1] == 'testmode':
            testmode = True
            open('log', 'w')

    run(testmode)

    if testmode:
        import os
        os.unlink('log')