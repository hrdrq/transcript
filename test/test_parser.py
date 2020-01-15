# -*- coding: utf-8 -*-
from unittest import TestCase

from parser import adv_to_adj, to_sentences, to_words

class ParseTest(TestCase):

    def test_adv_to_adj(self):
        adv1 = 'terribly'
        res1 = 'terrible'
        self.assertEqual(adv_to_adj(adv1), res1)

        adv2 = 'accidentally'
        res2 = 'accidental'
        self.assertEqual(adv_to_adj(adv2), res2)

        # not working
        adv3 = 'notably'
        # notable
        res3 = 'notably'
        self.assertEqual(adv_to_adj(adv3), res3)

        adv4 = 'happily'
        res4 = 'happy'
        self.assertEqual(adv_to_adj(adv4), res4)

    def test_sentence(self):
        doc1 = \
"""
Help me! Somebody, help me out.
Somebody, help me over here! Somebody, help me out! Oh, my God! Walt! Walt! Stay away from the gas! Stay there! Help! Help! Somebody, help me! Oh, my leg! Hey, get over here.
Give me a hand.
You, come on! Come over here! Give me a hand! On the count of three.
One, two, three! Help! Please, help me! Help me! Please, help me! Get him out of here.
Get him away from the engine.
Get him out of here.
Help me! Please, help me.
I'm having contractions! - How many months pregnant are you? - Only eight months.
- How far apart are they coming? - I don't know, a few just happened! Hey! Get away from there! Listen to me! Look at me! You're gonna be OK.
"""
        res1 = [
            'Help me! Somebody, help me out.',
            'Somebody, help me over here! Somebody, help me out! Oh, my God! Walt! Walt! Stay away from the gas! Stay there! Help! Help! Somebody, help me! Oh, my leg! Hey, get over here.',
            'Give me a hand.',
            'You, come on! Come over here! Give me a hand! On the count of three.',
            'One, two, three! Help! Please, help me! Help me! Please, help me! Get him out of here.',
            'Get him away from the engine.',
            'Get him out of here.',
            'Help me! Please, help me.',
            "I'm having contractions! - How many months pregnant are you? - Only eight months.",
            "How far apart are they coming? - I don't know, a few just happened! Hey! Get away from there! Listen to me! Look at me! You're gonna be OK."
        ]
        self.assertEqual(to_sentences(doc1), res1)

    def test_word(self):
        sen1 = "Help me! Somebody, help me out."
        res1 = ["help", "me", "somebody", "help", "me", "out"]
        self.assertEqual(to_words(sen1), res1)

        sen2 = 'Somebody, help me over here! Somebody, help me out! Oh, my God! Walt! Walt! Stay away from the gas! Stay there! Help! Help! Somebody, help me! Oh, my leg! Hey, get over here.'
        res2 = ['somebody', 'help', 'me', 'over', 'here', 'somebody', 'help', 'me', 'out', 'oh', 'my', 'God', 'Walt', 'Walt', 'stay', 'away', 'from', 'the', 'gas', 'stay', 'there', 'Help', 'Help', 'somebody', 'help', 'me', 'oh', 'my', 'leg', 'hey', 'get', 'over', 'here']
        self.assertEqual(to_words(sen2), res2)

        sen3 = "I'm having contractions! - How many months pregnant are you? - Only eight months."
        res3 = ['i', 'be', 'have', 'contraction', 'how', 'many', 'month', 'pregnant', 'be', 'you', 'only', 'eight', 'month']
        self.assertEqual(to_words(sen3), res3)

        sen4 = "And at the end, after 13 hours, I was closing her up and I I accidentally ripped her dural sack."
        res4 = ['and', 'at', 'the', 'end', 'after', 'hour', 'i', 'be', 'close', 'her', 'up', 'and', 'i', 'i', 'accidental', 'rip', 'her', 'dural', 'sack']
        self.assertEqual(to_words(sen4), res4)

        sen5 = "What makes you think we're any safer here than we are in the jungle? - Wait for me."
        res5 = ['what', 'make', 'you', 'think', 'we', 'be', 'any', 'safe', 'here', 'than', 'we', 'be', 'in', 'the', 'jungle', 'wait', 'for', 'me']
        self.assertEqual(to_words(sen5), res5)

        sen6 = "What? What are you talking about, you spent a year in Paris! - Drinking! Not studying! - Iteration 7-2-9-4-5-3-1 ."
        res6 = ['what', 'what', 'be', 'you', 'talk', 'about', 'you', 'spend', 'a', 'year', 'in', 'Paris', 'drink', 'not', 'study', 'iteration']
        self.assertEqual(to_words(sen6), res6)

        sen7 = "The pilot said we were over 1 ,000 miles off course."
        res7 = ['the', 'pilot', 'say', 'we', 'be', 'over', 'mile', 'off', 'course']
        self.assertEqual(to_words(sen7), res7)

        sen8 = "JIN: 내 옆에서 없어지면 안 돼. 내가 어디로 가든지 꼭 따라와. 알겠지? [Sun nods.] 다른 사람 신경쓰지 말고 우린 같이 있어야 돼."
        res8 = ['jin', 'Sun', 'nod']
        self.assertEqual(to_words(sen8), res8)
