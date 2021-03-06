#!/usr/bin/env python

# Copyright 2017-2018 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import SimpleITK as sitk
import fastr
import numpy as np
import os
import WORC.addexceptions as WORCexceptions

#WIP

class Transformix(object):
    def __init__(self):
        self.network = self.create_network()
        self.MovingImage = None
        self.TransformParameterMap = None

    def create_network(self):
        self.network = fastr.Network(id_="transformix")

        self.MovingImageSource = self.network.create_source('ITKImageFile', id_='MovingImage')
        self.ParameterMapSource = self.network.create_source('ElastixTransformFile', id_='ParameterFile')

        self.transformix_node = self.network.create_node('transformix_dev', id_='transformix')
        self.transformix_node.inputs['image'] = self.MovingImageSource.output
        self.transformix_node.inputs['transform'] = self.ParameterMapSource.output

        self.outimage = self.network.create_sink('ITKImageFile', id_='sink_image')
        self.outimage.inputs['input'] = self.transformix_node.outputs['image']

        self.network.draw_network(img_format='svg')
        self.network.dumpf('{}.json'.format(self.network.id), indent=2)

    def execute(self):
        SimpleTransformix = sitk.SimpleTransformix()
