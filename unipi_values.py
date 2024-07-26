##########################################################################
#
#  THIS FILE IS GENERATED FROM TEMPLATE. DON'T MODIFY IT
#
#  uniee_values.py
#
#  Created on: Jan 14, 2022
#      Author: Miroslav Ondra <ondra@faster.cz>
# 


class Product:
	def __init__(self, id, name, **kwargs):
		self.id = id
		self.name = name
		self.vars = kwargs

class Board:
	def __init__(self, id, name, slots, **kwargs):
		self.id = id
		self.name = name
		self.slots = slots
		self.vars = kwargs

class Slot:
	def __init__(self, slot, **kwargs):
		self.slot = slot
		self.vars = kwargs

products = {
  '1': Product(1, 'UNIPI10', dt='unipi_unipi10' , udev='unipi_unipi10' , has_ds2482='1' , has_rtc='1' , use_etc_modules='1' ),
  '257': Product(257, 'UNIPI11', dt='unipi_unipi11' , udev='unipi_unipi11' , has_ds2482='1' , has_rtc='1' , use_etc_modules='1' ),
  '4353': Product(4353, 'UNIPI1L', dt='unipi_unipi1l' , udev='unipi_unipi1l' , has_ds2482='1' , use_etc_modules='1' ),
}

boards = {
  '24': Board(24, 'EMO_R8',{
             '1': Slot(1, dt=['em0018_slot1'] , udev=['em0018_slot1'] , has_emor8_1='1'),
             '2': Slot(2, dt=['em0018_slot2'] , udev=['em0018_slot2'] , has_emor8_2='1'),
             '3': Slot(3, dt=['em0018_slot3'] , udev=['em0018_slot3'] , has_emor8_3='1'),
             '4': Slot(4, dt=['em0018_slot4'] , udev=['em0018_slot4'] , has_emor8_4='1'),
             '5': Slot(5, dt=['em0018_slot5'] , udev=['em0018_slot5'] , has_emor8_5='1'),
             '6': Slot(6, dt=['em0018_slot6'] , udev=['em0018_slot6'] , has_emor8_6='1'),
             '7': Slot(7, dt=['em0018_slot7'] , udev=['em0018_slot7'] , has_emor8_7='1'),
    }),
}

# Family names
family = {
  '1': 'UNIPI1',
  '2': 'G1XX',
  '3': 'NEURON',
  '5': 'AXON',
  '6': 'CM40',
  '7': 'PATRON',
  '15': 'IRIS',
  '16': 'OEM',
}

def unipi_product_info(product_id, version=None):
	''' return product_info or none '''
	return products.get(str(product_id), None)

def unipi_product_info_by_name(product_name, version=None):
	''' return product_info or none '''
	for k,v in products.items():
		if v.name.lower() == product_name.lower(): 
			return v
	short_name = product_name.lower()
	compare_len = len(short_name) - 1;
	while compare_len > 3:
		for k,v in products.items():
			if v.name.lower()[:compare_len] == short_name[:compare_len]: 
				return v
		compare_len -= 1

	return None

def unipi_board_info(board_id, slot=None, version=None):
	''' return board_info or None '''
	board_info = boards.get(str(board_id), None)
	if slot == None or board_info == None:
		return board_info
	if board_info.slots is None:
		return None
	return board_info.slots.get(str(slot), None)


def unipi_family_name(product_id):
	''' return family name or none '''
	return family.get(str(product_id & 0xff), None)
