import unittest
from inspect import signature, _ParameterKind
import numpy as np
import os
import sys
sys.path.append("..")
from characters import *

class TestHuman(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.args = {
            "name": "John",
            "health": 10,
            "power": 3,
            "accuracy": 50
        }
        cls.human = Human(**cls.args)
        cls.damage = 3
    
    def test_is_class(self):
        self.assertEqual(type(Human), type, "Human should be a class")
        
    def test_constructor_params(self):
        self.assertEqual(list(signature(Human).parameters.keys()), ['name', 'health', 'power', 'accuracy'], 
                         "Incorrect parameters for Human constructor.")
        
    def test_default_accuracy(self):
        self.assertEqual(signature(Human).parameters["accuracy"].default,50, "Default Accuracy should be 50 for Human")
    
    def test_attributes(self):
        vals = {self.args[param]:self.human.__getattribute__(param) for param in ['name', 'health', 'power', 'accuracy']}
        self.assertEqual(list(vals.keys()),list(vals.values()), "Attribute values not as expected.")
        
    def test_shoot(self):
        self.assertTrue(callable(self.human.shoot), "Can't call shoot method.")
        
    def test_shoot_accuracy(self):
        rep, exp = 1000, 1000
        shots = [[self.human.shoot() for _ in range(rep)] for _ in range(exp)]
        shots = [exp.count(0)/rep for exp in shots]
        shots = np.mean(shots)
        self.assertAlmostEqual(shots,.5,1, "Probability of shot is wrong.")
        
    def test_can_take_damage(self):
        self.assertTrue(callable(self.human.takeDamage), "Can't call takeDamage method.")
        
    def test_missed_shot(self):
        self.assertEqual(self.human.takeDamage(0), "Shot missed.", "Expected 'Shot missed.' for .takeDamage(0)")
        
    def test_shot_hit(self):
        self.assertEqual(self.human.takeDamage(self.damage), f"{self.human.name} lost {self.damage} health.", 
                         "Expected f'{human.name} lost {damage} health.' for .takeDamage(damage)")
        
    def test_looses_health(self):
        self.human.takeDamage(self.damage)
        self.assertEqual(self.human.health, self.args["health"]-self.damage, "Health should decrease after shot hits.")
    
    def test_can_die(self):
        res = self.human.takeDamage(100)
        self.assertEqual(res, f"{self.human.name} died.", 
                         "Expected f'{human.name} died.' when health <= 0")

class TestSniper(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.args = {
            "name": "John",
            "health": 10,
            "power": 3,
            "accuracy": 35
        }
        cls.sniper = Sniper(**cls.args)
        cls.damage = 3
    
    def test_is_class(self):
        self.assertEqual(type(Sniper), type, "Sniper should be a class")
        
    def test_constructor_params(self):
        self.assertEqual(list(signature(Sniper).parameters.keys()), ['name', 'health', 'power', 'accuracy'], 
                         "Incorrect parameters for Sniper constructor.")
        
    def test_default_accuracy(self):
        self.assertEqual(signature(Sniper).parameters["accuracy"].default,50, "Default Accuracy should be 50 for Sniper")
    
    def test_attributes(self):
        vals = {self.args[param]:self.sniper.__getattribute__(param) for param in ['name', 'health', 'power']}
        self.assertEqual(list(vals.keys()),list(vals.values()), "Attribute values not as expected.")
        
    def test_accuracy_boost(self):
        self.assertEqual(self.sniper.__getattribute__("accuracy"),self.args["accuracy"]+15,
                         "Sniper accuracy should have a 15 boost")
        
    def test_shoot(self):
        self.assertTrue(callable(self.sniper.shoot), "Can't call shoot method.")
        
    def test_shoot_accuracy(self):
        rep, exp = 1000, 1000
        shots = [[self.sniper.shoot() for _ in range(rep)] for _ in range(exp)]
        shots = [exp.count(0)/rep for exp in shots]
        shots = np.mean(shots)
        self.assertAlmostEqual(shots,.25,1, "Probability of shot is wrong.")
        
    def test_can_take_damage(self):
        self.assertTrue(callable(self.sniper.takeDamage), "Can't call takeDamage method.")
        
    def test_missed_shot(self):
        self.assertEqual(self.sniper.takeDamage(0), "Shot missed.", "Expected 'Shot missed.' for .takeDamage(0)")
        
    def test_shot_hit(self):
        self.assertEqual(self.sniper.takeDamage(self.damage), f"{self.sniper.name} lost {self.damage} health.", 
                         "Expected f'{sniper.name} lost {damage} health.' for .takeDamage(damage)")
        
    def test_looses_health(self):
        self.sniper.takeDamage(self.damage)
        self.assertEqual(self.sniper.health, self.args["health"]-self.damage, "Health should decrease after shot hits.")
    
    def test_can_die(self):
        res = self.sniper.takeDamage(100)
        self.assertEqual(res, f"{self.sniper.name} died.", 
                         "Expected f'{sniper.name} died.' when health <= 0")

class TestAlien(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.args = {
            "health": 10,
            "power": 3,
            "accuracy": 50
        }
        cls.alien = Alien(**cls.args)
        cls.damage = 3
    
    def test_is_class(self):
        self.assertEqual(type(Alien), type, "Alien should be a class")
        
    def test_constructor_params(self):
        self.assertEqual(list(signature(Alien).parameters.keys()), ['health', 'power', 'accuracy'], 
                         "Incorrect parameters for Alien constructor.")
        
    def test_default_accuracy(self):
        self.assertEqual(signature(Alien).parameters["accuracy"].default,65, "Default Accuracy should be 65 for Alien")
    
    def test_attributes(self):
        vals = {self.args[param]:self.alien.__getattribute__(param) for param in ['health', 'power', 'accuracy']}
        self.assertEqual(list(vals.keys()),list(vals.values()), "Attribute values not as expected.")
        
    def test_shoot(self):
        self.assertTrue(callable(self.alien.shoot), "Can't call shoot method.")
        
    def test_shoot_accuracy(self):
        rep, exp = 1000, 1000
        shots = [[self.alien.shoot() for _ in range(rep)] for _ in range(exp)]
        shots = [exp.count(0)/rep for exp in shots]
        shots = np.mean(shots)
        self.assertAlmostEqual(shots,.5,1, "Probability of shot is wrong.")
        
    def test_can_take_damage(self):
        self.assertTrue(callable(self.alien.takeDamage), "Can't call takeDamage method.")
        
    def test_missed_shot(self):
        self.assertEqual(self.alien.takeDamage(0), "Shot missed.", "Expected 'Shot missed.' for .takeDamage(0)")
        
    def test_shot_hit(self):
        self.assertEqual(self.alien.takeDamage(self.damage), f"Alien lost {self.damage} health.", 
                         "Expected f'Alien lost {damage} health.' for .takeDamage(damage)")
        
    def test_looses_health(self):
        self.alien.takeDamage(self.damage)
        self.assertEqual(self.alien.health, self.args["health"]-self.damage, "Health should decrease after shot hits.")
    
    def test_can_die(self):
        res = self.alien.takeDamage(100)
        self.assertEqual(res, "Alien scum destroyed.", 
                         "Expected 'Alien scum destroyed.' when health <= 0")
        
class TestSquad(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.args = {
            "name": "John",
            "health": 10,
            "power": 3,
            "accuracy": 50
        }
        cls.human = Human(**cls.args)
        cls.damage = 3
        cls.squad = Squad(cls.human)
    
    def test_is_class(self):
        self.assertEqual(type(Squad), type, "Squad should be a class")
        
    def test_n_fighters(self):
        self.assertEqual(signature(Squad).parameters["fighters"].kind, _ParameterKind.VAR_POSITIONAL,
                         "Squad should accept as many fighters as you pass.")
        
    def test_add(self):
        self.assertTrue(callable(self.squad.add), "Can't call add method.")
        
    def test_added_fighter(self):
        fig = Alien(10,3)
        self.squad.add(fig)
        self.assertTrue(fig in self.squad.fighters, "Fighter not added to self.fighters.")
    
    def test_remove(self):
        self.assertTrue(callable(self.squad.remove), "Can't call remove method.")
        
    def test_removed_fighter(self):
        self.squad.remove(self.human)
        self.assertFalse(self.human in self.squad.fighters, "Fighter not removed from self.fighters.")
        
    def test_len(self):
        self.assertTrue(callable(self.squad.__len__), "__len__ not implemented")
        
    def test_len_value(self):
        [self.squad.add(Alien(10,3)) for _ in range(12)]
        self.assertEqual(len(self.squad), len(self.squad.fighters), "__len__ does not return len of self.fighters")
        
    def test_iter(self):
        self.assertTrue(callable(self.squad.__iter__), "__iter__ not implemented")
        
    def test_iter_value(self):
        [self.squad.add(Alien(10,3)) for _ in range(12)]
        self.assertTrue(all((a==b for a,b in zip(iter(self.squad), iter(self.squad.fighters)))), 
                            "__iter__ does not return iter(self.fighters)")

class TestBattle(unittest.TestCase):
    @classmethod
    def setUp(cls):
        class MockHuman:
            def __init__(self, name, health, power):
                self.name =  name
                self.health = health
                self.power = power
            def shoot(self):
                return self.power
            def takeDamage(self, damage):
                self.health -= damage
                if damage == 0:
                    return "Shot missed."
                elif self.health >= 0:
                    return f"{self.name} lost {damage} health."
                else:
                    return f"{self.name} died."
        class MockAlien(MockHuman):
            def __init__(self, health, power):
                super().__init__("Alien", health, power)
            def takeDamage(self,damage):
                if damage >= self.health:
                    self.health -= damage
                    return "Alien scum destroyed."
                else:
                    return super().takeDamage(damage)
        class MockSquad:
            def __init__(self,*fighters):
                self.fighters = list(fighters)
                self.add = lambda fig : self.fighters.append(fig)
                self.remove = lambda fig : self.fighters.remove(fig)
            __len__ = lambda self: self.fighters.__len__()
            __iter__ = lambda self: self.fighters.__iter__()
                
        cls.humans = MockSquad(*[MockHuman("J",10,i) for i in [0,1,100]])
        cls.worthless = MockSquad(*[MockHuman("J",10,0) for _ in range(3)])
        cls.regular = MockSquad(*[MockHuman("J",10,1) for _ in range(3)])
        cls.elite = MockSquad(*[MockHuman("J",10,100) for _ in range(3)])
        cls.aliens = MockSquad(*[MockAlien(10,i) for i in [0,0,0]])
        cls.battle = Battle(cls.aliens,cls.humans)
        cls.empty = MockSquad()
        cls.human = MockSquad(MockHuman("J",3,1))
        cls.alien = MockSquad(MockAlien(3,1))
        cls.make_battle = lambda self: Battle(MockSquad(MockAlien(3,100)),MockSquad(MockHuman("J",3,100)))
    
    def test_is_class(self):
        self.assertEqual(type(Battle), type, "Battle should be a class")
        
    def test_constructor_params(self):
        self.assertEqual(list(signature(Battle).parameters.keys()), ["aliens", "humans"], 
                         "Incorrect parameters for Battle constructor.")
        
    def test_attack(self):
        self.assertTrue(callable(self.battle.attack), "Can't call attack method.")
        
    def test_attack_value(self):
        res = self.battle.attack(self.humans,self.aliens)
        self.assertEqual(res, {"shots_missed":1,"shots_hit":1,"enemies_killed":1},
                         "attack method did not return expected result.")

    def test_attack_all_miss(self):
        res = self.battle.attack(self.worthless,self.aliens)
        self.assertEqual(res, {"shots_missed":3,"shots_hit":0,"enemies_killed":0},
                         "attack method did not return expected result.")
        
    def test_attack_all_hit(self):
        res = self.battle.attack(self.regular,self.aliens)
        self.assertEqual(res, {"shots_missed":0,"shots_hit":3,"enemies_killed":0},
                         "attack method did not return expected result.")
        
    def test_attack_all_kill(self):
        res = self.battle.attack(self.elite,self.aliens)
        self.assertEqual(res, {"shots_missed":0,"shots_hit":0,"enemies_killed":3},
                         "attack method did not return expected result.")
        
    def test_dead_removed(self):
        res = self.battle.attack(self.humans,self.aliens)
        removed = len(self.aliens) == 2
        living = all([al.health > 0 for al in self.aliens])
        self.assertTrue(removed and living, "dead fighters not properly removed in 'attack' method")
        
    def test_status(self):
        self.assertTrue(callable(self.battle.status), "Can't call status method.")
        
    def test_no_humans(self):
        self.assertEqual(Battle(self.worthless,self.empty).status(),"The human race failed. Aliens conquered the Earth.",
                        "Aliens should win if there are no humans")
        
    def test_no_aliens(self):
        self.assertEqual(Battle(self.empty,self.worthless).status(),"Humans saved the Earth. The planet is still ours, for now.",
                        "Humans should win if there are no aliens")
    
    def test_status(self):
        self.assertEqual(Battle(self.worthless,self.elite).status(),"The battle goes on. Our planet depends on it.",
                        "Expected 'The battle goes on. Our planet depends on it.' if there are soldiers on both sides")
    
    def test_status_change(self):
        battle = Battle(self.elite,self.worthless)
        first = battle.status()
        battle.attack(self.elite, self.worthless)
        second = battle.status()
        self.assertEqual((first,second),("The battle goes on. Our planet depends on it.","The human race failed. Aliens conquered the Earth."),
                        "Status should change after victory")