import sqlite3
import os
import sys
from discord import *
from discord.ext import *
from discord.ext.commands import *
import asyncio

conn = sqlite3.connect("Storage.db")
colour = sys.stdout.shell
c = conn.cursor()
bot = Bot(command_prefix='owo ')

if __name__ == '__main__':
    colour.write("*** ERROR - LAUNCHING INCORRECT FILE***\n",'COMMENT')
    quit()

try:

    c.execute("""CREATE TABLE trainers (
                ID text,
                gold text,
                badges text,
                region text
                )
    """)

    
    c.execute("""CREATE TABLE monsters (
                monster text,
                health text,
                attack text,
                defence text,
                special_attack text,
                special_defence text,
                speed text,
                typing text,
                ability text
                )
    """)

    c.execute("""CREATE TABLE dakumon (
                monster text,
                level text,
                name text,
                health text,
                attack text,
                defence text,
                special_attack text,
                special_defence text,
                speed text,
                typing text,
                ability text,
                owner text
                ID text,
                )
    """)

    c.execute("""CREATE TABLE moves (
                move text,
                damage text,
                typing text,
                category text,
                accuracy text,
                PP text,
                critical text,
                effect text
                )
    """)

except:
    pass

class Table:

    def __init__(self,*arg):
        self.created = True
        self.table_list.append(self)
        self.primary = reference_wrapper(0)
        
    def instantiate_variables(self,*arg):
        self.default_stats()
        for (count,variable) in enumerate(arg):
            setattr(self,self.stats[count], reference_wrapper(variable)) 

    def change_stat(self,stat,value,add=False):
        if stat not in self.stats:
            return "Argument is invalid"
        attempt = self.function_mapper[stat](value,stat,getattr(self,stat),add)
        return attempt

    def change_base_stat(self,change,target_stat,current_stat,add=False):
        if add:
            current_stat.value = str(int(current_stat.value)+int(change))
        else:
            current_stat.value = str(change)
        return "Successfully updated "+str(getattr(self,self.stats[0]))+"'s "+target_stat    

    def add_to_stat(self,change,target_stat,current_stat,add=False):
        if add and len(current_stat.value) != 0:
           current_stat.value += ", "+str(change)
        else:
            current_stat.value = str(change)
        return "Successfully updated "+str(getattr(self,self.stats[0]))+"'s "+target_stat

    def default_stats(self):
        pass
            
    @classmethod
    def save(cls):
        
        table_list = globals()[cls.__name__.lower()+"_list"]
        for target in table_list:
            instruction = "SELECT * FROM "+target.table+" WHERE "+target.stats[int(target.primary)]+" = ?"
            c.execute(instruction, (str(getattr(target,target.stats[int(target.primary)]).value),))
            if c.fetchone():
                instruction = "UPDATE "+target.table+" SET "+'=?, '.join(target.stats)+"=? WHERE "+str(target.stats[int(target.primary)])+"=?"
                c.execute(instruction, list(map(lambda stat: str(getattr(target, stat)),target.stats))+[(str(getattr(target,target.stats[int(target.primary)])))])
            else:
                instruction = "INSERT INTO "+target.table+" VALUES (:"+', :'.join(target.stats)+")"
                c.execute(instruction, dict(zip(target.stats,list(map(lambda stat: str(getattr(target, stat)),target.stats)))))
        conn.commit()

    @classmethod
    def remove(cls,ID):
        table_list = globals()[cls.__name__.lower()+"_list"]
        print("DELETING "+cls.__name__.upper())
        target = cls.get(ID)
        if target:
            table_list.remove(target)
        instruction = "SELECT * FROM "+target.table+" WHERE "+target.stats[int(target.primary)]+" = ?"
        c.execute(instruction, (ID,))
        if c.fetchone():
            instruction = "DELETE FROM "+target.table+" WHERE "+target.stats[int(target.primary)]+" = ?"
            c.execute(instruction, (ID,))
        print("SUCCESSFULLY DELETED")

    @staticmethod
    async def load(table):
        constructor = dict(zip(table_names,table_class))
        instruction = "SELECT * FROM "+table
        c.execute(instruction)
        for target in c.fetchall():
            print("="*30)
            try:
                user = ''
                if table == 'trainers':
                    user = await bot.get_user_info(target[0])
                constructor[table](*target,trainer=user)
            except Exception as e:
                print(e)
                print("Target with ID "+str(target[target.primary])+" cannot be located in our server; subsequently, they have been removed from my database")
                print("Relationships will also get wiped")
                (constructor[table]).remove(target[target.primary])
                
            print("="*30)

    @classmethod
    def get(cls,ID):
        target_list = globals()[cls.__name__.lower()+"_list"]
        return next((target for target in target_list if str(getattr(target, target.stats[int(target.primary)])) == str(ID)), None)


class Trainer(Table):
    
    def __init__(self,*arg,**kwargs):
        self.table_list = trainer_list
        self.table = 'trainers'
        super(Trainer,self).__init__(*arg)
        self.trainer = kwargs['trainer']
        self.stats = ['ID','gold','badges','region']
        self.functions = [self.change_ID,self.change_base_stat,self.add_to_stat,self.add_to_stat]
        self.instantiate_variables(*arg)
        self.function_mapper = dict(zip(self.stats, self.functions))

        for stat in self.stats:
            print(stat.capitalize()+": "+str(getattr(self,stat)))

    def default_stats(self):
        self.gold = reference_wrapper(10)
        self.badges = reference_wrapper('Red')
        self.region = reference_wrapper('Island')

    def change_ID(self,change,target_stat,current_stat,add=False):
        return 'This feature is not yet implemented'
        

class Monster(Table):
    
    def __init__(self,*arg,**kwargs):
        self.table_list = monster_list
        self.table = 'monsters'
        super(Monster,self).__init__(*arg)
        self.stats = ['monster','health','attack','defence','special_attack','special_defence','speed','typing','ability']
        self.functions = [self.change_monster,self.change_base_stat,self.change_base_stat,self.change_base_stat,self.change_base_stat,self.change_base_stat,self.change_base_stat,self.change_base_stat,self.change_base_stat]
        self.instantiate_variables(*arg)
        self.function_mapper = dict(zip(self.stats, self.functions))

        for stat in self.stats:
            print(stat.capitalize()+": "+str(getattr(self,stat)))

    def change_monster(self,change,target_stat,current_stat,add=False):
        return 'This feature is not yet implemented'

    def default_stats(self):
        self.ability = reference_wrapper('None')


class Dakumon(Table):
    
    def __init__(self,*arg,**kwargs):
        self.table_list = dakumon_list
        self.table = 'dakumon'
        super(Dakumon,self).__init__(*arg)
        self.stats = ['monster','level','name','health','attack','defence','special_attack','special_defence','speed','typing','ability','owner','ID']
        self.functions = [self.change_monster,self.change_level,self.change_base_stat,self.change_base_stat,self.change_base_stat,self.change_base_stat,self.change_base_stat,self.change_base_stat,self.change_base_stat,self.change_base_stat,self.change_owner,self.change_ID]
        self.instantiate_variables(*arg)
        self.function_mapper = dict(zip(self.stats, self.functions))

        for stat in self.stats:
            print(stat.capitalize()+": "+str(getattr(self,stat)))

    def change_monster(self,change,target_stat,current_stat,add=False):
        return 'This feature is not yet implemented'

    def change_ID(self,change,target_stat,current_stat,add=False):
        return 'This feature is not yet implemented'

    def change_owner(self,change,target_stat,current_stat,add=False):
        return 'This feature is not yet implemented'

    def change_level(self,change,target_stat,current_stat,add=False):
        return 'This feature is not yet implemented'

    def default_stats(self):
        self.ID = reference_wrapper(0)
        self.ID = reference_wrapper(self.get_ID())
        self.owner = reference_wrapper('None')
        self.ability = reference_wrapper('None')
        self.primary = reference_wrapper(12)

    def get_ID(self):
        print(dakumon_list)
        sorted_list = sorted(dakumon_list, key=lambda dakumon: int(dakumon.ID))
        for (count,dakumon) in enumerate(sorted_list):
            print(count,dakumon.ID)
            if count != int(dakumon.ID):
                return reference_wrapper(count)
        return reference_wrapper(len(dakumon_list))

class reference_wrapper:
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return(self.value)
    def __add__(self, other):
        return (self.value) + other
    def __int__(self):
        return int(self.value)



for subclass in Table.__subclasses__():
    print(subclass.__name__)
    globals()[subclass.__name__.lower()+"_list"] = []
    table_list = []
    table_list.append(globals()[subclass.__name__.lower()+"_list"])
    
dakumon_monster_list = []

table_names = ['trainers','monsters','dakumon']
table_class = [Trainer,Monster,Dakumon]

table_dict = dict(zip(map(lambda klass: klass.__name__,table_class),table_names))
