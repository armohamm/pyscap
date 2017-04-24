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

from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class BenchmarkType(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'status', 'append': 'statuses', 'class': 'StatusType', 'min': 1, 'max': None},
            {'xml_namespace': 'http://purl.org/dc/elements/1.1/', 'tag_name': 'dc-status', 'append': 'dc_statuses', 'class': 'DCStatusType', 'min': 0, 'max': None},
            {'tag_name': 'title', 'append': 'titles', 'class': 'TextType', 'min': 0, 'max': None},
            {'tag_name': 'description', 'append': 'descriptions', 'class': 'HTMLTextWithSubType', 'min': 0, 'max': None},
            {'tag_name': 'notice', 'map': 'notices', 'class': 'NoticeType', 'min': 0, 'max': None},
            {'tag_name': 'front-matter', 'append': 'front_matter', 'class': 'HtmlTextWithSubType', 'min': 0, 'max': None},
            {'tag_name': 'rear-matter', 'append': 'rear_matter', 'class': 'HtmlTextWithSubType', 'min': 0, 'max': None},
            {'tag_name': 'reference', 'append': 'references', 'class': 'ReferenceType', 'min': 0, 'max': None},
            {'tag_name': 'plain-text', 'append': 'plain_texts', 'class': 'PlainTextType', 'min': 0, 'max': None},
            {'xml_namespace': 'http://cpe.mitre.org/language/2.0', 'tag_name': 'platform-specification', 'class': 'scap.model.cpe_lang_2_3.PlatformSpecificationType', 'min': 0, 'max': 1},
            {'tag_name': 'platform', 'class': 'CPE2IDRefType', 'min': 0, 'max': None},
            {'tag_name': 'version', 'class': 'VersionType', 'min': 1, 'max': 1},
            {'tag_name': 'metadata', 'append': 'metadata', 'class': 'MetadataType', 'min': 0, 'max': None},
            {'tag_name': 'model', 'append': 'models', 'class': 'ModelType', 'min': 0, 'max': None},
            {'tag_name': 'Profile', 'class': 'ProfileType', 'min': 0, 'max': None, 'map': 'profiles'},
            {'tag_name': 'Value', 'class': 'ValueType', 'min': 0, 'max': None, 'map': 'values'},
            {'tag_name': 'Group', 'class': 'GroupType', 'min': 0, 'max': None, 'map': 'groups'},
            {'tag_name': 'Rule', 'class': 'RuleType', 'min': 0, 'max': None, 'map': 'rules'},
            {'tag_name': 'TestResult', 'class': 'TestResultType', 'min': 0, 'max': None, 'map': 'tests'},
            {'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': 1},
        ],
        'attributes': {
            'id': {'required': True, 'type': 'BenchmarkIDPattern'},
            'Id': {'type': 'ID'},
            'resolved': {'type': 'Boolean', 'default': False},
            'style': {'type': 'String'},
            'style-href': {'type': 'AnyURI'},
        },
    }
