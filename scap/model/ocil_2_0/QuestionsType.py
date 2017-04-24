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
class QuestionsType(Model):
    MODEL_MAP = {
        'elements': [
            #TODO: at least one of the following *_question elements
            {'tag_name': 'boolean_question', 'append': 'questions', 'class': 'BooleanQuestionElement', 'min': 0, 'max': None},
            {'tag_name': 'choice_question', 'append': 'questions', 'class': 'ChoiceQuestionElement', 'min': 0, 'max': None},
            {'tag_name': 'numeric_question', 'append': 'questions', 'class': 'NumericQuestionElement', 'min': 0, 'max': None},
            {'tag_name': 'string_question', 'append': 'questions', 'class': 'StringQuestionElement', 'min': 0, 'max': None},
            {'tag_name': 'choice_group', 'append': 'questions', 'class': 'ChoiceGroupType', 'min': 0, 'max': None},
        ],
    }
