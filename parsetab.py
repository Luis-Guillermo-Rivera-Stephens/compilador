
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATTRIBUTE BOOLEAN COMA DOS_PUNTOS L_CORCHETE L_LLAVE NULL NUMBER R_CORCHETE R_LLAVE STRINGjson : object\n            | arrayobject : L_LLAVE key_value_list R_LLAVE\n              | L_LLAVE R_LLAVEkey_value_list : key_value\n                      | key_value COMA key_value_listkey_value : ATTRIBUTE value\n                | STRING DOS_PUNTOS valuearray : L_CORCHETE value_list R_CORCHETE\n             | L_CORCHETE R_CORCHETEvalue_list : value\n                  | value COMA value_listvalue : object\n             | array\n             | STRING\n             | NUMBER\n             | BOOLEAN\n             | NULL'
    
_lr_action_items = {'L_LLAVE':([0,5,9,23,25,],[4,4,4,4,4,]),'L_CORCHETE':([0,5,9,23,25,],[5,5,5,5,5,]),'$end':([1,2,3,7,12,20,24,],[0,-1,-2,-4,-10,-3,-9,]),'R_LLAVE':([4,6,7,8,12,14,15,16,17,18,19,20,22,24,26,27,],[7,20,-4,-5,-10,-13,-14,-15,-16,-17,-18,-3,-7,-9,-6,-8,]),'ATTRIBUTE':([4,21,],[9,9,]),'STRING':([4,5,9,21,23,25,],[10,16,16,10,16,16,]),'R_CORCHETE':([5,7,11,12,13,14,15,16,17,18,19,20,24,28,],[12,-4,24,-10,-11,-13,-14,-15,-16,-17,-18,-3,-9,-12,]),'NUMBER':([5,9,23,25,],[17,17,17,17,]),'BOOLEAN':([5,9,23,25,],[18,18,18,18,]),'NULL':([5,9,23,25,],[19,19,19,19,]),'COMA':([7,8,12,13,14,15,16,17,18,19,20,22,24,27,],[-4,21,-10,25,-13,-14,-15,-16,-17,-18,-3,-7,-9,-8,]),'DOS_PUNTOS':([10,],[23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'json':([0,],[1,]),'object':([0,5,9,23,25,],[2,14,14,14,14,]),'array':([0,5,9,23,25,],[3,15,15,15,15,]),'key_value_list':([4,21,],[6,26,]),'key_value':([4,21,],[8,8,]),'value_list':([5,25,],[11,28,]),'value':([5,9,23,25,],[13,22,27,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> json","S'",1,None,None,None),
  ('json -> object','json',1,'p_json','yacc_file.py',5),
  ('json -> array','json',1,'p_json','yacc_file.py',6),
  ('object -> L_LLAVE key_value_list R_LLAVE','object',3,'p_object','yacc_file.py',10),
  ('object -> L_LLAVE R_LLAVE','object',2,'p_object','yacc_file.py',11),
  ('key_value_list -> key_value','key_value_list',1,'p_key_value_list','yacc_file.py',18),
  ('key_value_list -> key_value COMA key_value_list','key_value_list',3,'p_key_value_list','yacc_file.py',19),
  ('key_value -> ATTRIBUTE value','key_value',2,'p_key_value','yacc_file.py',26),
  ('key_value -> STRING DOS_PUNTOS value','key_value',3,'p_key_value','yacc_file.py',27),
  ('array -> L_CORCHETE value_list R_CORCHETE','array',3,'p_array','yacc_file.py',34),
  ('array -> L_CORCHETE R_CORCHETE','array',2,'p_array','yacc_file.py',35),
  ('value_list -> value','value_list',1,'p_value_list','yacc_file.py',42),
  ('value_list -> value COMA value_list','value_list',3,'p_value_list','yacc_file.py',43),
  ('value -> object','value',1,'p_value','yacc_file.py',50),
  ('value -> array','value',1,'p_value','yacc_file.py',51),
  ('value -> STRING','value',1,'p_value','yacc_file.py',52),
  ('value -> NUMBER','value',1,'p_value','yacc_file.py',53),
  ('value -> BOOLEAN','value',1,'p_value','yacc_file.py',54),
  ('value -> NULL','value',1,'p_value','yacc_file.py',55),
]
