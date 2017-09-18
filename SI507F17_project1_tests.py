## Do not change import statements.
import unittest
import requests
from SI507F17_project1_cards import *
from helper_functions import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

class test_class_card(unittest.TestCase):

	def setUp(self):
		self.c1=Card(3,3)

	def test_suit_class_variable(self):
		self.assertEqual(self.c1.suit_names , ["Diamonds","Clubs","Hearts","Spades"])
		self.assertEqual(self.c1.rank_levels , [1,2,3,4,5,6,7,8,9,10,11,12,13])
		self.assertEqual(self.c1.faces,{1:"Ace",11:"Jack",12:"Queen",13:"King"})

	def test_suit_constructor(self):
		self.assertEqual(self.c1.suit,"Spades")#should I set up an integer or use variable here?
		self.assertEqual(self.c1.rank_num,4)

	def test_suit_output(self):
		self.assertEqual(str(self.c1),"4 of Spades",'test the string method')


class test_class_deck(unittest.TestCase):

	def setUp(self):
		self.d = Deck()

	def test_deck_constructor(self):
		self.assertIsInstance(self.d.cards,list)
		self.assertEqual(len(self.d.cards),52)
		self.assertIsInstance(self.d.cards[2],Card)
		self.assertIn(self.d.cards[3].rank, range(1,14))
		self.assertIn(self.d.cards[3].suit, range(1,4))

	def test_deck_printer(self):
		self.assertIsInstance(str(self.d),str)######

	def test_method_pop_card(self):
		self.d.pop_card(6)
		self.assertIsInstance(self.d.cards, list)
		self.assertEqual(len(self.d.cards),46)

	def test_method_shuffle(self):
		#self.assertNotEqual(d2.cards[3],d.cards[3])#cannot shuffle one card, just the list's order #get strings of cards
		self.d2 = self.d.shuffle()
		self.cards_strings=[str(c) for c in self.d.cards]#before shuffle
		self.cards_strings_shuffled=[str(c) for c in self.d2.cards]#after shuffle
		self.assertNotEqual(cards_strings,cards_strings_shuffled)
	def test_replace_card(self):#not have any duplicated cards
		self.d.replace_card(self.d.cards[10])
		self.assertEqual(len(self.d.cards),len(set(self.d.cards)))

	def test_sort_cards(self):
		self.assertTrue(self.d.cards[10].suit<=self.d.cards[11].suit)
	
	def  test_deal_hand(self):
		self.assertIsInstance(self.d.deal_hand(5),list)#返回list，拿在手里的5张牌
		self.assertIsInstance((self.d.deal_hand(5))[0],Card)
		self.assertIn(len(self.d.deal_hand(10)),range(42))

class test_play_war_game(unittest.TestCase):

	def test_play_func(self):
		self.assertIsInstance(play_war_game(testing=True),tuple)
		self.tu = play_war_game(testing=True)
		if self.tu[1]<self.tu[2]:
			self.assertEqual(self.tu[0],"Player2")
		elif self.tu[1]>self.tu[2]:
			self.assertEqual(self.tu[0],"Player1")
		else:
			self.assertEqual(self.tu[0],"tie")

class show_song(unittest.TestCase):
	def test_show_song(self):
		self.song = show_song("Hello")
		self.assertIsInstance(self.song, Song)
		self.s2 = show_song('Bowie')#testing if the function search for the song you expected
		self.assertTrue('Bowie' in str(self.s2))

unittest.main(verbosity=2)

###########