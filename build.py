#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Adobe Flex Build system - connect to flex remote compile shell and run build

from rook.de import flex
import time
import os
import shutil

sdk = flex.SDK('4.9.1')

sdk.swf('Robotlegs2Test', 'src/example/Main.mxml',
        output='bin/Robotlegs2Test.swf', 
        requires=[l[:-4] for l in os.listdir('libs/') if l.endswith('swc')],
        args=['-static-link-runtime-shared-libraries=true', '-debug'])
