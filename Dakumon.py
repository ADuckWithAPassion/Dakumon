from Dakubase import *

@bot.event
async def on_ready():
    colour.write("*** LOADING TRAINERS ***\n","STRING")
    await Trainer.load('trainers')
    colour.write("*** LOADING MONSTERS ***\n","STRING")
    await Monster.load('monsters')
    colour.write("*** LOADING DAKUMON ***\n","STRING")
    await Monster.load('dakumon')

@bot.command(pass_context=True)
async def create_trainer(ctx,*arg):
    if len(list(arg)) == 1:
        try:
            trainer = await bot.get_user_info(arg[0])
        except:
            await bot.send_message(ctx.message.channel, "ID is about as wrong as a woman not being in the kitchen")
            return    
        if Trainer.get(arg[0]): 
            await bot.send_message(ctx.message.channel, "User already exists")
            return
        if(Trainer(*arg,trainer=trainer).created):
            await bot.send_message(ctx.message.channel, "Successfully created trainer account")
        else:
            await bot.send_message(ctx.message.channel, "Error occurred in creation of trainer")
    else:
        await bot.send_message(ctx.message.channel, "owo create_trainer [ID]")

@bot.command(pass_context=True)
async def create_monster(ctx,*arg):
    if len(list(arg)) in [8,9]:
        if Monster.get(arg[0]):
            await bot.send_message(ctx.message.channel, "Monster already exists")
            return
        if(Monster(*arg).created):
            await bot.send_message(ctx.message.channel, "Successfully created monster")
        else:
            await bot.send_message(ctx.message.channel, "Error occurred in creation of monster")
    else:
        await bot.send_message(ctx.message.channel, "owo create_monster [Monster] [Health] [Attack] [Defence] [Special Attack] [Special Defence] [Speed] [Typing] [Ability]")

@bot.command(pass_context=True)
async def create_dakumon(ctx,*arg):
    if len(list(arg)) in [10,11,12,13]:
        if len(list(arg)) == 13 and Dakumon.get(arg[-1]):
            await bot.send_message(ctx.message.channel, "Dakumon already exists")
            return
        if(Dakumon(*arg).created):
            await bot.send_message(ctx.message.channel, "Successfully created dakumon")
        else:
            await bot.send_message(ctx.message.channel, "Error occurred in creation of dakumon")
    else:
        await bot.send_message(ctx.message.channel, "owo create_dakumon [Monster] [Level] [Name] [Health] [Attack] [Defence] [Special Attack] [Special Defence] [Speed] [Typing] {Ability} {Owner} {ID}")

@bot.command(pass_context=True)
async def change_trainer_stat(ctx,*arg):
    if (len(list(arg)) == 3 or len(list(arg)) == 4):
        trainer = Trainer.get(arg[0])
        if trainer:
            attempt = trainer.change_stat(*arg[1::])
            return await bot.send_message(ctx.message.channel,attempt)    
        else:
            await bot.send_message(ctx.message.channel,"ID is invalid")    
    else:
        await bot.send_message(ctx.message.channel,"owo change_trainer_stat [ID] [Stat] [Value] {Add}")

@bot.command(pass_context=True)
async def change_monster_stat(ctx,*arg):
    if (len(list(arg)) == 3 or len(list(arg)) == 4):
        monster = Monster.get(arg[0])
        if monster:
            attempt = monster.change_stat(*arg[1::])
            return await bot.send_message(ctx.message.channel,attempt)    
        else:
            await bot.send_message(ctx.message.channel,"Monster is invalid")    
    else:
        await bot.send_message(ctx.message.channel,"owo change_monster_stat [Monster] [Stat] [Value] {Add}")

@bot.command(pass_context=True)
async def change_dakumon_stat(ctx,*arg):
    if (len(list(arg)) == 3 or len(list(arg)) == 4):
        dakumon = Dakumon.get(arg[0])
        if dakumon:
            attempt = dakumon.change_stat(*arg[1::])
            return await bot.send_message(ctx.message.channel,attempt)    
        else:
            await bot.send_message(ctx.message.channel,"ID is invalid")    
    else:
        await bot.send_message(ctx.message.channel,"owo change_dakumon_stat [ID] [Stat] [Value] {Add}")

@bot.command(pass_context=True)
async def remove_trainer(ctx,*arg):
    if len(list(arg)) == 1:
        trainer = Trainer.get_trainer(arg[0])
        if trainer:
            Trainer.remove(arg[0])
            await bot.send_message(ctx.message.channel,"Trainer no longer exists")    
        else:
            await bot.send_message(ctx.message.channel,"ID is invalid")
    else:
        await bot.send_message(ctx.message.channel,"owo remove_trainer [ID]")    

@bot.command(pass_context=True)
async def remove_monster(ctx,*arg):
    if len(list(arg)) == 1:
        monster = Monster.get_monster(arg[0])
        if monster:
            Monster.remove(arg[0])
            await bot.send_message(ctx.message.channel,"Monster no longer exists")    
        else:
            await bot.send_message(ctx.message.channel,"Monster is invalid")    
    else:
        await bot.send_message(ctx.message.channel,"owo remove_monster [Monster]")    

@bot.command(pass_context=True)
async def remove_dakumon(ctx,*arg):
    if len(list(arg)) == 1:
        dakumon = Dakumon.get_dakumon(arg[0])
        if dakumon:
            Dakumon.remove(arg[0])
            await bot.send_message(ctx.message.channel,"Dakumon no longer exists")    
        else:
            await bot.send_message(ctx.message.channel,"ID is invalid")    
    else:
        await bot.send_message(ctx.message.channel,"owo remove_dakumon [ID]")    


@bot.command(pass_context=True)
async def save(ctx,*arg):
    if len(list(arg)) == 0:
        colour.write("*** SAVING TRAINERS ***\n","STRING")
        Trainer.save()
        colour.write("*** SAVING MONSTERS ***\n","STRING")
        Monster.save()
        colour.write("*** SAVING DAKUMON ***\n","STRING")
        Dakumon.save()
        await bot.send_message(ctx.message.channel,"Successfully Saved")
    else:
        await bot.send_message(ctx.message.channel,"owo save")
        

    
bot.run("NDYwNTI5ODc5NjI5MTY4NjUx.DhGFkw.6Sw5il46CYUhL-UkjW9SEHFs4vQ")
