# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

import logging
import datetime

from scap.Model import Model

from scap.model.xccdf_1_1.ModelType import ModelType

logger = logging.getLogger(__name__)
class BenchmarkType(Model):
    MODEL_MAP = {
        'tag_name': 'Benchmark',
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}status': {'append': 'statuses', 'class': 'StatusElement', 'min': 1, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}title': {'append': 'titles', 'class': 'TextType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}description': {'append': 'descriptions', 'class': 'HTMLTextWithSubType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}notice': {'map': 'notices', 'class': 'NoticeType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}front-matter': {'append': 'front_matter', 'class': 'HtmlTextWithSubType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}rear-matter': {'append': 'rear_matter', 'class': 'HtmlTextWithSubType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}reference': {'append': 'references', 'class': 'ReferenceType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}plain-text': {'append': 'plain_texts', 'class': 'PlainTextType', 'min': 0, 'max': None},
            # TODO choice of one of the following
            # CIS Platform schema, compatibility with XCCDF 1.0
            '{http://www.cisecurity.org/xccdf/platform/0.2.3}platform-definitions': {'class': 'scap.model.xccdf_platform_0_2_3.PlatformDefinitionsType', 'min': 0, 'max': 1},
            # XCCDF-P 1.0 schema, compatibility with XCCDF 1.1
            '{http://checklists.nist.gov/xccdf-p/1.1}Platform-Specification': {'class': 'scap.model.xccdf_p_1_1.PlatformSpecificationType', 'min': 0, 'max': 1},
            # CPE 1.0 schema, compatibility with XCCDF 1.1.3
            '{http://cpe.mitre.org/XMLSchema/cpe/1.0}cpe-list': {'class': 'scap.model.cpe_1_0.CpeListType', 'min': 0, 'max': 1},
            # CPE 2.0 language schema, for SCAP 1.0 conformance
            '{http://cpe.mitre.org/language/2.0}platform-specification': {'class': 'scap.model.cpe_lang_2_3.PlatformSpecificationType', 'min': 0, 'max': 1},

            '{http://checklists.nist.gov/xccdf/1.1}platform': {'class': 'UriIdrefType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}version': {'class': 'VersionType', 'min': 1, 'max': 1},
            '{http://checklists.nist.gov/xccdf/1.1}metadata': {'append': 'metadata', 'class': 'MetadataType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}model': {'append': 'models', 'class': 'ModelType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}Profile': {'class': 'ProfileType', 'min': 0, 'max': None, 'map': 'profiles'},
            '{http://checklists.nist.gov/xccdf/1.1}Value': {'class': 'ValueType', 'min': 0, 'max': None, 'map': 'items'},
            '{http://checklists.nist.gov/xccdf/1.1}Group': {'class': 'GroupType', 'min': 0, 'max': None, 'map': 'items'},
            '{http://checklists.nist.gov/xccdf/1.1}Rule': {'class': 'RuleType', 'min': 0, 'max': None, 'map': 'items'},
            '{http://checklists.nist.gov/xccdf/1.1}TestResult': {'class': 'TestResultType', 'min': 0, 'max': None, 'map': 'test_results'},
            '{http://checklists.nist.gov/xccdf/1.1}signature': {'class': 'SignatureType', 'min': 0, 'max': 1},
        },
        'attributes': {
            'id': {'required': True, 'type': 'NCName'},
            'Id': {'type': 'ID'},
            'resolved': {'type': 'Boolean', 'default': False},
            'style': {'type': 'String'},
            'style-href': {'type': 'AnyURI'},
        },
    }

    def __str__(self):
        return self.__class__.__name__ + ' # ' + self.id

    def noticing(self):
        ### Loading.Noticing

        # For each notice property of the Benchmark object, add the notice to
        # the tool’s set of legal notices. If a notice with an identical id
        # value is already a member of the set, then replace it. If the
        # Benchmark’s resolved property is set, then Loading succeeds, otherwise
        # go to the next step: Loading.Resolve.Items.

        for notice in list(self.notices.values()):
            logger.info('Notice: \n' + str(notice))

    def resolve(self):
        if self.resolved:
            return

        ### Loading.Resolve.Items

        for item_id in self.items:
            logger.debug('Resolving item: ' + item_id)
            self.items[item_id].resolve(self)

        ### Loading.Resolve.Profiles

        for profile_id in self.profiles:
            if self.profiles[profile_id].extends:
                logger.debug('Resolving profile: ' + profile_id)
                self.profiles[profile_id].resolve(self)

        ### Loading.Resolve.Abstract

        # For each Item in the Benchmark for which the abstract property is
        # true, remove the Item.
        for item_id in self.items:
            if self.items[item_id].abstract:
                logger.debug('Deleting abstract item: ' + item_id)
                del self.items[item_id]

        # For each Profile in the Benchmark for which the abstract property is
        # true, remove the Profile. Go to the next step:
        # Loading.Resolve.Finalize
        for profile_id in self.profiles:
            if self.profiles[profile_id].abstract:
                logger.debug('Deleting abstract profile: ' + profile_id)
                del self.profiles[profile_id]

        ### Loading.Resolve.Finalize

        # Set the Benchmark resolved property to true; Loading succeeds.
        self.resolved = True

    def process(self, host):
        ### Benchmark.Front

        if 'checklist' not in host.facts:
            host.facts['checklist'] = {}

        if self.id not in host.facts['checklist']:
            host.facts['checklist'][self.id] = {
                'start_time': datetime.datetime.utcnow(),
                'profile': {},
            }

        # Process the properties of the Benchmark object

        # TODO check that if this benchmark has a platform specification identified,
        # that the  target system matches

        # TODO check that if this benchmark has a platform identified, that the
        # target system matches

        ### Benchmark.Profile

        if not hasattr(self, 'selected_profiles'):
            raise ValueError('No profiles have been selected for Benchmark ' + self.id)

        for profile_id in self.selected_profiles:
            logger.info('Selecting profile ' + str(profile_id))
            if profile_id not in host.facts['checklist'][self.id]['profile']:
                host.facts['checklist'][self.id]['profile'][profile_id] = {
                    'start_time': datetime.datetime.utcnow(),
                    'rule': {},
                    'value': {},
                    'scores': [],
                }
            self.profiles[profile_id].apply(host, self)

            ### Benchmark.Content

            # For each Item in the Benchmark object’s items property, initiate
            # Item.Process
            for item in self.items.values():
                item.process(host, self, profile_id)

            if len(self.models) == 0:
                def_model = ModelType(tag_name='model')
                def_model.system = 'urn:xccdf:scoring:default'
                self.models.append(def_model)

            for model in self.models:
                model.score(host, self, profile_id)

            host.facts['checklist'][self.id]['profile'][profile_id]['end_time'] =  datetime.datetime.utcnow()
        ### Benchmark.Back

        # Perform any additional processing of the Benchmark object properties
        host.facts['checklist'][self.id]['end_time'] =  datetime.datetime.utcnow()
