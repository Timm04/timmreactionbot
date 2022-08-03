from cgitb import text
from http.client import responses
from imaplib import Commands
from multiprocessing.sharedctypes import Value
from posixpath import split
from pydoc import describe
from random import choices
from secrets import choice
from turtle import color
import discord
import regex as re
import asyncio
import datetime
import time
from numpy import sort
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import date
from datetime import datetime
from datetime import timedelta
import datetime
from discord.ext.commands import CommandNotFound
from pytz import HOUR,country_names
import re
import random
import collections
import pandas as pd
import sqlite3
from pathlib import Path
import MySQLdb
from discord.ext import commands
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import bot

import json
import os

if os.path.exists(os.getcwd() + "/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "", "Prefix": "!"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 

token = configData["Token"]
prefix = configData["Prefix"]


intents = discord.Intents.all()
client = commands.Bot(command_prefix="!",intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_raw_reaction_add(payload):

        if payload.message_id != 1004453416019443772:
            return

        guild = client.get_guild(payload.guild_id)

        emoji_names = ['🇦🇨','🇦🇩','🇦🇪','🇦🇫','🇦🇬',
                   '🇦🇮','🇦🇱','🇦🇲','🇦🇴','🇦🇶',
                   '🇦🇷','🇦🇸','🇦🇹','🇦🇺','🇦🇼',
                   '🇦🇽','🇦🇿','🇧🇦','🇧🇧','🇧🇩',
                   '🇧🇪','🇧🇫','🇧🇬','🇧🇭','🇧🇮',
                   '🇧🇯','🇧🇱','🇧🇲','🇧🇳','🇧🇴',
                   '🇧🇶','🇧🇷','🇧🇸','🇧🇹','🇧🇻',
                   '🇧🇼','🇧🇾','🇧🇿','🇨🇦','🇨🇨',
                   '🇨🇩','🇨🇫','🇨🇬','🇨🇭','🇨🇮',
                   '🇨🇰','🇨🇱','🇨🇲','🇨🇳','🇨🇴','🇨🇵',
                   '🇨🇷','🇨🇺','🇨🇻','🇨🇼','🇨🇽',
                   '🇨🇾','🇨🇿','🇩🇪','🇩🇬','🇩🇯','🇩🇰',
                   '🇩🇲','🇩🇴','🇩🇿','🇪🇦','🇪🇨','🇪🇪',
                   '🇪🇬','🇪🇭','🇪🇷','🇪🇸','🇪🇹','🇪🇺',
                   '🇫🇮','🇫🇯','🇫🇰','🇫🇲','🇫🇴',
                   '🇫🇷','🇬🇦','🇬🇧','🇬🇩','🇬🇪',
                   '🇬🇫','🇬🇬','🇬🇭','🇬🇮','🇬🇱',
                   '🇬🇲','🇬🇳','🇬🇵','🇬🇶','🇬🇷',
                   '🇬🇸','🇬🇹','🇬🇺','🇬🇼','🇬🇾',
                   '🇭🇰','🇭🇲','🇭🇳','🇭🇷','🇭🇹',
                   '🇭🇺','🇮🇨','🇮🇩','🇮🇪','🇮🇱','🇮🇲',
                   '🇮🇳','🇮🇴','🇮🇶','🇮🇷','🇮🇸',
                   '🇮🇹','🇯🇪','🇯🇲','🇯🇴','🇯🇵',
                   '🇰🇪','🇰🇬','🇰🇭','🇰🇮','🇰🇲',
                   '🇰🇳','🇰🇵','🇰🇷','🇰🇼','🇰🇾',
                   '🇰🇿','🇱🇦','🇱🇧','🇱🇨','🇱🇮',
                   '🇱🇰','🇱🇷','🇱🇸','🇱🇹','🇱🇺',
                   '🇱🇻','🇱🇾','🇲🇦','🇲🇨','🇲🇩',
                   '🇲🇪','🇲🇫','🇲🇬','🇲🇭','🇲🇰',
                   '🇲🇱','🇲🇲','🇲🇳','🇲🇴','🇲🇵','🇲🇶',
                   '🇲🇷','🇲🇸','🇲🇹','🇲🇺','🇲🇻','🇲🇼',
                   '🇲🇽','🇲🇾','🇲🇿','🇳🇦','🇳🇨','🇳🇪','🇳🇫',
                   '🇳🇬','🇳🇮','🇳🇱','🇳🇴','🇳🇵',
                   '🇳🇷','🇳🇺','🇳🇿','🇴🇲','🇵🇦','🇵🇪',
                   '🇵🇫','🇵🇬','🇵🇭','🇵🇰','🇵🇱',
                   '🇵🇲','🇵🇳','🇵🇷','🇵🇸','🇵🇹',
                   '🇵🇼','🇵🇾','🇶🇦','🇷🇪','🇷🇴','🇷🇸',
                   '🇷🇺','🇷🇼','🇸🇦','🇸🇧','🇸🇨','🇸🇩',
                   '🇸🇪','🇸🇬','🇸🇭','🇸🇮','🇸🇯',
                   '🇸🇰','🇸🇱','🇸🇲',
                   '🇸🇳','🇸🇴',
                   '🇸🇷','🇸🇸','🇸🇹','🇸🇻','🇸🇽','🇸🇾',
                   '🇸🇿','🇹🇦','🇹🇨','🇹🇩','🇹🇫','🇹🇬','🇹🇭','🇹🇯','🇹🇰',
                   '🇹🇱','🇹🇲','🇹🇳','🇹🇴',
                   '🇹🇷','🇹🇹',
                   '🇹🇻','🇹🇼','🇹🇿','🇺🇦','🇺🇬','🇺🇲','🇺🇳',
                   '🇺🇸','🇺🇾','🇺🇿','🇻🇦','🇻🇨','🇻🇪',
                   '🇻🇬','🇻🇮','🇻🇳','🇻🇺',
                   '🇼🇫','🇼🇸','🇽🇰','🇾🇪','🇾🇹','🇿🇦','🇿🇲','🇿🇼', '🏴‍☠️']

        country_names = ['Ascension Island','Andorra','United Arab Emirates','Afghanistan','Antigua & Barbuda',
                     'Anguilla','Albania','Armenia','Angola','Antarctica',
                     'Argentina','American Samoa','Austria','Australia','Aruba',
                     'Åland Islands','Azerbaijan','Bosnia & Herzegovina','Barbados','Bangladesh',
                     'Belgium','Burkina Faso','Bulgaria','Bahrain','Burundi',
                     'Benin','St. Barthélemy','Bermuda','Brunei','Bolivia',
                     'Caribbean Netherlands','Brazil','Bahamas','Bhutan','Bouvet Island',
                     'Botswana','Belarus','Belize','Canada','Cocos(Keeling) Islands',
                     'Congo - Kinshasa','Central African Republic','Congo - Brazzaville','Switzerland','Côte d’Ivoire',
                     'Cook Islands','Chile','Cameroon','China','Colombia',
                     'Clipperton Island','Costa Rica','Cuba','Cape Verde','Curaçao',
                     'Christmas Island','Cyprus','Czechia','Germany','Diego Garcia','Djibouti','Denmark',
                     'Dominica','Dominican Republic','Algeria','Ceuta & Melilla','Ecuador','Estonia',
                     'Egypt','Western Sahara','Eritrea','Spain','Ethiopia',
                     'European Union','Finland','Fiji','Falkland Islands','Micronesia','Faroe Islands',
                     'France','Gabon','United Kingdom','Grenada','Georgia',
                     'French Guiana','Guernsey','Ghana','Gibraltar','Greenland',
                     'Gambia','Guinea','Guadeloupe','Equatorial','Greece',
                     'South Georgia & South Sandwich Islands','Guatemala','Guam','Guinea-Bissau','Guyana',
                     'Hong Kong SAR China','Heard & McDonald Islands','Honduras','Croatia','Haiti',
                     'Hungary','Canary Islands','Indonesia','Ireland','Israel','Isle of Man',
                     'India','British Indian Ocean Territory','Iraq','Iran','Iceland',
                     'Italy','Jersey','Jamaica','Jordan','Japan',
                     'Kenya','Kyrgyzstan','Cambodia','Kiribati','Comoros',
                     'St. Kitts & Nevis','North Korea','South Korea','Kuwait',
                     'Cayman Islands','Kazakhstan','Laos','Lebanon','St. Lucia','Liechtenstein',
                     'Sri Lanka','Liberia','Lesotho','Lithuania','Luxembourg',
                     'Latvia','Libya','Morocco','Monaco','Moldova',
                     'Montenegro','St. Martin','Madagascar','Marshall Islands','North Macedonia',
                     'Mali','Myanmar(Burma)','Mongolia','Macao Sar China','Northern Mariana Islands','Martinique',
                     'Mauritania','Montserrat','Malta','Mauritius','Maldives','Malawi','Mexico','Malaysia',
                     'Mozambique','Namibia','New Caledonia','Niger','Norfolk Island','Nigeria','Nicaragua',
                     'Netherlands','Norway','Nepal','Nauru','Niue','New Zealand','Oman','Panama','Peru','French Polynesia',
                     'Papua New Guinea','Philippines','Pakistan','Poland','St. Pierre & Miquelon','Pitcairn Islands',
                     'Puerto Rico','Palestinian Territories','Portugal','Palau','Paraguay','Qatar','Réunion','Romania',
                     'Serbia','Russia','Rwanda','Saudi Arabia','Solomon Islands','Seychelles','Sudan','Sweden','Singapore',
                     'St. Helena','Slovenia','Svalbard & Jan Mayen','Slovakia','Sierra Leone','San Marino','Senegal',
                     'Somalia','Suriname','South Sudan','🇸🇹São Tomé & Príncipe','El Salvador','Sint Maarten','Syria',
                     'Eswatini','Tristan Da Cunha','Turks & Caicos Islands','Chad','French Southern Territories','Togo',
                     'Thailand','Tajikistan','Tokelau','Timor-Leste','Turkmenistan','Tunisia','Tonga','Turkey','Trinidad & Tobago',
                     'Tuvalu','Taiwan','Tanzania','Ukraine','Uganda','U.S. Outlying Islands','United Nations','United States',
                     'Uruguay','Uzbekistan','Vatican City','St. Vincent & Grenadines','Venezuela','British Virgin Islands',
                     'U.S. Virgin Islands','Vietnam','Vanuatu','Wallis & Futuna','Samoa','Kosovo','Yemen','Mayotte','South Africa','Zambia','Zimbabwe', 'Pirate']
        
        emoji_lists = list(zip(emoji_names,country_names))
        for (x,y) in emoji_lists:
            if payload.emoji.name == x:
                print("reaction emote is in list")
                if y not in [str(r.name) for r in guild.roles]:
                    print("role doesnt exist so creating one")
                    role = await guild.create_role(name=y,colour=discord.Colour(0x000000))
                    get_role = discord.utils.get(guild.roles, name=y)
                    await payload.member.add_roles(role)
                    print("giving role")
                elif y in [str(r.name) for r in guild.roles]:
                    print("role exists so fiving")
                    role = discord.utils.get(guild.roles, name=y)
                    await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):


        if payload.message_id != 1004453416019443772:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)


        emoji_names = ['🇦🇨','🇦🇩','🇦🇪','🇦🇫','🇦🇬',
                   '🇦🇮','🇦🇱','🇦🇲','🇦🇴','🇦🇶',
                   '🇦🇷','🇦🇸','🇦🇹','🇦🇺','🇦🇼',
                   '🇦🇽','🇦🇿','🇧🇦','🇧🇧','🇧🇩',
                   '🇧🇪','🇧🇫','🇧🇬','🇧🇭','🇧🇮',
                   '🇧🇯','🇧🇱','🇧🇲','🇧🇳','🇧🇴',
                   '🇧🇶','🇧🇷','🇧🇸','🇧🇹','🇧🇻',
                   '🇧🇼','🇧🇾','🇧🇿','🇨🇦','🇨🇨',
                   '🇨🇩','🇨🇫','🇨🇬','🇨🇭','🇨🇮',
                   '🇨🇰','🇨🇱','🇨🇲','🇨🇳','🇨🇴','🇨🇵',
                   '🇨🇷','🇨🇺','🇨🇻','🇨🇼','🇨🇽',
                   '🇨🇾','🇨🇿','🇩🇪','🇩🇬','🇩🇯','🇩🇰',
                   '🇩🇲','🇩🇴','🇩🇿','🇪🇦','🇪🇨','🇪🇪',
                   '🇪🇬','🇪🇭','🇪🇷','🇪🇸','🇪🇹','🇪🇺',
                   '🇫🇮','🇫🇯','🇫🇰','🇫🇲','🇫🇴',
                   '🇫🇷','🇬🇦','🇬🇧','🇬🇩','🇬🇪',
                   '🇬🇫','🇬🇬','🇬🇭','🇬🇮','🇬🇱',
                   '🇬🇲','🇬🇳','🇬🇵','🇬🇶','🇬🇷',
                   '🇬🇸','🇬🇹','🇬🇺','🇬🇼','🇬🇾',
                   '🇭🇰','🇭🇲','🇭🇳','🇭🇷','🇭🇹',
                   '🇭🇺','🇮🇨','🇮🇩','🇮🇪','🇮🇱','🇮🇲',
                   '🇮🇳','🇮🇴','🇮🇶','🇮🇷','🇮🇸',
                   '🇮🇹','🇯🇪','🇯🇲','🇯🇴','🇯🇵',
                   '🇰🇪','🇰🇬','🇰🇭','🇰🇮','🇰🇲',
                   '🇰🇳','🇰🇵','🇰🇷','🇰🇼','🇰🇾',
                   '🇰🇿','🇱🇦','🇱🇧','🇱🇨','🇱🇮',
                   '🇱🇰','🇱🇷','🇱🇸','🇱🇹','🇱🇺',
                   '🇱🇻','🇱🇾','🇲🇦','🇲🇨','🇲🇩',
                   '🇲🇪','🇲🇫','🇲🇬','🇲🇭','🇲🇰',
                   '🇲🇱','🇲🇲','🇲🇳','🇲🇴','🇲🇵','🇲🇶',
                   '🇲🇷','🇲🇸','🇲🇹','🇲🇺','🇲🇻','🇲🇼',
                   '🇲🇽','🇲🇾','🇲🇿','🇳🇦','🇳🇨','🇳🇪','🇳🇫',
                   '🇳🇬','🇳🇮','🇳🇱','🇳🇴','🇳🇵',
                   '🇳🇷','🇳🇺','🇳🇿','🇴🇲','🇵🇦','🇵🇪',
                   '🇵🇫','🇵🇬','🇵🇭','🇵🇰','🇵🇱',
                   '🇵🇲','🇵🇳','🇵🇷','🇵🇸','🇵🇹',
                   '🇵🇼','🇵🇾','🇶🇦','🇷🇪','🇷🇴','🇷🇸',
                   '🇷🇺','🇷🇼','🇸🇦','🇸🇧','🇸🇨','🇸🇩',
                   '🇸🇪','🇸🇬','🇸🇭','🇸🇮','🇸🇯',
                   '🇸🇰','🇸🇱','🇸🇲',
                   '🇸🇳','🇸🇴',
                   '🇸🇷','🇸🇸','🇸🇹','🇸🇻','🇸🇽','🇸🇾',
                   '🇸🇿','🇹🇦','🇹🇨','🇹🇩','🇹🇫','🇹🇬','🇹🇭','🇹🇯','🇹🇰',
                   '🇹🇱','🇹🇲','🇹🇳','🇹🇴',
                   '🇹🇷','🇹🇹',
                   '🇹🇻','🇹🇼','🇹🇿','🇺🇦','🇺🇬','🇺🇲','🇺🇳',
                   '🇺🇸','🇺🇾','🇺🇿','🇻🇦','🇻🇨','🇻🇪',
                   '🇻🇬','🇻🇮','🇻🇳','🇻🇺',
                   '🇼🇫','🇼🇸','🇽🇰','🇾🇪','🇾🇹','🇿🇦','🇿🇲','🇿🇼', '🏴‍☠️']

        country_names = ['Ascension Island','Andorra','United Arab Emirates','Afghanistan','Antigua & Barbuda',
                     'Anguilla','Albania','Armenia','Angola','Antarctica',
                     'Argentina','American Samoa','Austria','Australia','Aruba',
                     'Åland Islands','Azerbaijan','Bosnia & Herzegovina','Barbados','Bangladesh',
                     'Belgium','Burkina Faso','Bulgaria','Bahrain','Burundi',
                     'Benin','St. Barthélemy','Bermuda','Brunei','Bolivia',
                     'Caribbean Netherlands','Brazil','Bahamas','Bhutan','Bouvet Island',
                     'Botswana','Belarus','Belize','Canada','Cocos(Keeling) Islands',
                     'Congo - Kinshasa','Central African Republic','Congo - Brazzaville','Switzerland','Côte d’Ivoire',
                     'Cook Islands','Chile','Cameroon','China','Colombia',
                     'Clipperton Island','Costa Rica','Cuba','Cape Verde','Curaçao',
                     'Christmas Island','Cyprus','Czechia','Germany','Diego Garcia','Djibouti','Denmark',
                     'Dominica','Dominican Republic','Algeria','Ceuta & Melilla','Ecuador','Estonia',
                     'Egypt','Western Sahara','Eritrea','Spain','Ethiopia',
                     'European Union','Finland','Fiji','Falkland Islands','Micronesia','Faroe Islands',
                     'France','Gabon','United Kingdom','Grenada','Georgia',
                     'French Guiana','Guernsey','Ghana','Gibraltar','Greenland',
                     'Gambia','Guinea','Guadeloupe','Equatorial','Greece',
                     'South Georgia & South Sandwich Islands','Guatemala','Guam','Guinea-Bissau','Guyana',
                     'Hong Kong SAR China','Heard & McDonald Islands','Honduras','Croatia','Haiti',
                     'Hungary','Canary Islands','Indonesia','Ireland','Israel','Isle of Man',
                     'India','British Indian Ocean Territory','Iraq','Iran','Iceland',
                     'Italy','Jersey','Jamaica','Jordan','Japan',
                     'Kenya','Kyrgyzstan','Cambodia','Kiribati','Comoros',
                     'St. Kitts & Nevis','North Korea','South Korea','Kuwait',
                     'Cayman Islands','Kazakhstan','Laos','Lebanon','St. Lucia','Liechtenstein',
                     'Sri Lanka','Liberia','Lesotho','Lithuania','Luxembourg',
                     'Latvia','Libya','Morocco','Monaco','Moldova',
                     'Montenegro','St. Martin','Madagascar','Marshall Islands','North Macedonia',
                     'Mali','Myanmar(Burma)','Mongolia','Macao Sar China','Northern Mariana Islands','Martinique',
                     'Mauritania','Montserrat','Malta','Mauritius','Maldives','Malawi','Mexico','Malaysia','Mozambique',
                     'Namibia','New Caledonia','Niger','Norfolk Island','Nigeria','Nicaragua','Netherlands','Norway',
                     'Nepal','Nauru','Niue','New Zealand','Oman','Panama','Peru','French Polynesia','Papua New Guinea',
                     'Philippines','Pakistan','Poland','St. Pierre & Miquelon','Pitcairn Islands','Puerto Rico',
                     'Palestinian Territories','Portugal','Palau','Paraguay','Qatar','Réunion','Romania','Serbia',
                     'Russia','Rwanda','Saudi Arabia','Solomon Islands','Seychelles','Sudan','Sweden','Singapore',
                     'St. Helena','Slovenia','Svalbard & Jan Mayen','Slovakia','Sierra Leone','San Marino','Senegal',
                     'Somalia','Suriname','South Sudan','🇸🇹São Tomé & Príncipe','El Salvador','Sint Maarten','Syria',
                     'Eswatini','Tristan Da Cunha','Turks & Caicos Islands','Chad','French Southern Territories','Togo',
                     'Thailand','Tajikistan','Tokelau','Timor-Leste','Turkmenistan','Tunisia','Tonga','Turkey','Trinidad & Tobago',
                     'Tuvalu','Taiwan','Tanzania','Ukraine','Uganda','U.S. Outlying Islands','United Nations','United States',
                     'Uruguay','Uzbekistan','Vatican City','St. Vincent & Grenadines','Venezuela','British Virgin Islands',
                     'U.S. Virgin Islands','Vietnam','Vanuatu','Wallis & Futuna','Samoa','Kosovo','Yemen','Mayotte','South Africa','Zambia','Zimbabwe', 'Pirate']
        
        emoji_lists = list(zip(emoji_names,country_names))
        for (x,y) in emoji_lists:
            if payload.emoji.name == x:
                role = discord.utils.get(guild.roles, name=y)
                await member.remove_roles(role)

client.run(os.environ["DISCORD_TOKEN"])
        #         if y not in [str(r.name) for r in guild.roles]:
        #             print("role doesnt exist so creating one")
        #             role = await guild.create_role(name=y,colour=discord.Colour(0x000000))
        #             get_role = discord.utils.get(guild.roles, name=y)
        #             await payload.member.add_roles(role)
        #             print("giving role")
        #         elif y in [str(r.name) for r in guild.roles]:
        #             print("role exists so fiving")
        #             role = discord.utils.get(guild.roles, name=y)
        #             await payload.member.add_roles(role)

        # if payload.emoji.name == '(Your emoji)':
        #     role = discord.utils.get(guild.roles, name='<Your role>')
        #     await member.remove_roles(role)


# @client.command()
# async def reaction_setup(ctx):
#     username = ctx.message.author.name
#     channel = client.get_channel(1003015576869937183)
#     message = await channel.send("**Role Menu: Country**" + "\n" +
#     "React with the flag of where you come from to give yourself a role.")
#     global msg
#     msg = message.id
    

# @client.event
# async def on_reaction_add(reaction,ctx):
#         emoji_names = ['🇦🇨','🇦🇩','🇦🇪','🇦🇫','🇦🇬',
#                    '🇦🇮','🇦🇱','🇦🇲','🇦🇴','🇦🇶',
#                    '🇦🇷','🇦🇸','🇦🇹','🇦🇺','🇦🇼',
#                    '🇦🇽','🇦🇿','🇧🇦','🇧🇧','🇧🇩',
#                    '🇧🇪','🇧🇫','🇧🇬','🇧🇭','🇧🇮',
#                    '🇧🇯','🇧🇱','🇧🇲','🇧🇳','🇧🇴',
#                    '🇧🇶','🇧🇷','🇧🇸','🇧🇹','🇧🇻',
#                    '🇧🇼','🇧🇾','🇧🇿','🇨🇦','🇨🇨',
#                    '🇨🇩','🇨🇫','🇨🇬','🇨🇭','🇨🇮',
#                    '🇨🇰','🇨🇱','🇨🇲','🇨🇳','🇨🇴','🇨🇵',
#                    '🇨🇷','🇨🇺','🇨🇻','🇨🇼','🇨🇽',
#                    '🇨🇾','🇨🇿','🇩🇪','🇩🇬','🇩🇯','🇩🇰',
#                    '🇩🇲','🇩🇴','🇩🇿','🇪🇦','🇪🇨','🇪🇪',
#                    '🇪🇬','🇪🇭','🇪🇷','🇪🇸','🇪🇹','🇪🇺',
#                    '🇫🇮','🇫🇯','🇫🇰','🇫🇲','🇫🇴',
#                    '🇫🇷','🇬🇦','🇬🇧','🇬🇩','🇬🇪',
#                    '🇬🇫','🇬🇬','🇬🇭','🇬🇮','🇬🇱',
#                    '🇬🇲','🇬🇳','🇬🇵','🇬🇶','🇬🇷',
#                    '🇬🇸','🇬🇹','🇬🇺','🇬🇼','🇬🇾',
#                    '🇭🇰','🇭🇲','🇭🇳','🇭🇷','🇭🇹',
#                    '🇭🇺','🇮🇨','🇮🇩','🇮🇪','🇮🇱','🇮🇲',
#                    '🇮🇳','🇮🇴','🇮🇶','🇮🇷','🇮🇸',
#                    '🇮🇹','🇯🇪','🇯🇲','🇯🇴','🇯🇵',
#                    '🇰🇪','🇰🇬','🇰🇭','🇰🇮','🇰🇲',
#                    '🇰🇳','🇰🇵','🇰🇷','🇰🇼','🇰🇾',
#                    '🇰🇿','🇱🇦','🇱🇧','🇱🇨','🇱🇮',
#                    '🇱🇰','🇱🇷','🇱🇸','🇱🇹','🇱🇺',
#                    '🇱🇻','🇱🇾','🇲🇦','🇲🇨','🇲🇩',
#                    '🇲🇪','🇲🇫','🇲🇬','🇲🇭','🇲🇰',
#                    '🇲🇱','🇲🇲','🇲🇳','🇲🇴','🇲🇵','🇲🇶',
#                    '🇲🇷','🇲🇸','🇲🇹','🇲🇺','🇲🇻','🇲🇼',
#                    '🇲🇽','🇲🇾','🇲🇿','🇳🇦','🇳🇨','🇳🇪','🇳🇫',
#                    '🇳🇬','🇳🇮','🇳🇱','🇳🇴','🇳🇵',
#                    '🇳🇷','🇳🇺','🇳🇿','🇴🇲','🇵🇦','🇵🇪',
#                    '🇵🇫','🇵🇬','🇵🇭','🇵🇰','🇵🇱',
#                    '🇵🇲','🇵🇳','🇵🇷','🇵🇸','🇵🇹',
#                    '🇵🇼','🇵🇾','🇶🇦','🇷🇪','🇷🇴','🇷🇸',
#                    '🇷🇺','🇷🇼','🇸🇦','🇸🇧','🇸🇨','🇸🇩',
#                    '🇸🇪','🇸🇬','🇸🇭','🇸🇮','🇸🇯',
#                    '🇸🇰','🇸🇱','🇸🇲',
#                    '🇸🇳','🇸🇴',
#                    '🇸🇷','🇸🇸','🇸🇹','🇸🇻','🇸🇽','🇸🇾',
#                    '🇸🇿','🇹🇦','🇹🇨','🇹🇩','🇹🇫','🇹🇬','🇹🇭','🇹🇯','🇹🇰',
#                    '🇹🇱','🇹🇲','🇹🇳','🇹🇴',
#                    '🇹🇷','🇹🇹',
#                    '🇹🇻','🇹🇼','🇹🇿','🇺🇦','🇺🇬','🇺🇲','🇺🇳',
#                    '🇺🇸','🇺🇾','🇺🇿','🇻🇦','🇻🇨','🇻🇪',
#                    '🇻🇬','🇻🇮','🇻🇳','🇻🇺',
#                    '🇼🇫','🇼🇸','🇽🇰','🇾🇪','🇾🇹','🇿🇦','🇿🇲','🇿🇼']

#         country_names = ['Ascension Island','Andorra','United Arab Emirates','Afghanistan','Antigua & Barbuda',
#                      'Anguilla','Albania','Armenia','Angola','Antarctica',
#                      'Argentina','American Samoa','Austria','Australia','Aruba',
#                      'Åland Islands','Azerbaijan','Bosnia & Herzegovina','Barbados','Bangladesh',
#                      'Belgium','Burkina Faso','Bulgaria','Bahrain','Burundi',
#                      'Benin','St. Barthélemy','Bermuda','Brunei','Bolivia',
#                      'Caribbean Netherlands','Brazil','Bahamas','Bhutan','Bouvet Island',
#                      'Botswana','Belarus','Belize','Canada','Cocos(Keeling) Islands',
#                      'Congo - Kinshasa','Central African Republic','Congo - Brazzaville','Switzerland','Côte d’Ivoire',
#                      'Cook Islands','Chile','Cameroon','China','Colombia',
#                      'Clipperton Island','Costa Rica','Cuba','Cape Verde','Curaçao',
#                      'Christmas Island','Cyprus','Czechia','Germany','Diego Garcia','Djibouti','Denmark',
#                      'Dominica','Dominican Republic','Algeria','Ceuta & Melilla','Ecuador','Estonia',
#                      'Egypt','Western Sahara','Eritrea','Spain','Ethiopia',
#                      'European Union','Finland','Fiji','Falkland Islands','Micronesia','Faroe Islands',
#                      'France','Gabon','United Kingdom','Grenada','Georgia',
#                      'French Guiana','Guernsey','Ghana','Gibraltar','Greenland',
#                      'Gambia','Guinea','Guadeloupe','Equatorial','Greece',
#                      'South Georgia & South Sandwich Islands','Guatemala','Guam','Guinea-Bissau','Guyana',
#                      'Hong Kong SAR China','Heard & McDonald Islands','Honduras','Croatia','Haiti',
#                      'Hungary','Canary Islands','Indonesia','Ireland','Israel','Isle of Man',
#                      'India','British Indian Ocean Territory','Iraq','Iran','Iceland',
#                      'Italy','Jersey','Jamaica','Jordan','Japan',
#                      'Kenya','Kyrgyzstan','Cambodia','Kiribati','Comoros',
#                      'St. Kitts & Nevis','North Korea','South Korea','Kuwait',
#                      'Cayman Islands','Kazakhstan','Laos','Lebanon','St. Lucia','Liechtenstein',
#                      'Sri Lanka','Liberia','Lesotho','Lithuania','Luxembourg',
#                      'Latvia','Libya','Morocco','Monaco','Moldova',
#                      'Montenegro','St. Martin','Madagascar','Marshall Islands','North Macedonia',
#                      'Mali','Myanmar(Burma)','Mongolia','Macao Sar China','Northern Mariana Islands','Martinique',
#                      'Mauritania','Montserrat','Malta','Mauritius','Maldives','Malawi','Mexico','Malaysia','Mozambique','Namibia','New Caledonia','Niger','Norfolk Island','Nigeria','Nicaragua','Netherlands','Norway','Nepal','Nauru','Niue','New Zealand','Oman','Panama','Peru','French Polynesia','Papua New Guinea','Philippines','Pakistan','Poland','St. Pierre & Miquelon','Pitcairn Islands','Puerto Rico','Palestinian Territories','Portugal','Palau','Paraguay','Qatar','Réunion','Romania','Serbia','Russia','Rwanda','Saudi Arabia','Solomon Islands','Seychelles','Sudan','Sweden','Singapore','St. Helena','Slovenia','Svalbard & Jan Mayen','Slovakia','Sierra Leone','San Marino','Senegal','Somalia','Suriname','South Sudan','🇸🇹São Tomé & Príncipe','El Salvador','Sint Maarten','Syria','Eswatini','Tristan Da Cunha','Turks & Caicos Islands','Chad','French Southern Territories','Togo','Thailand','Tajikistan','Tokelau','Timor-Leste','Turkmenistan','Tunisia','Tonga','Turkey','Trinidad & Tobago','Tuvalu','Taiwan','Tanzania','Ukraine','Uganda','U.S. Outlying Islands','United Nations','United States','Uruguay','Uzbekistan','Vatican City','St. Vincent & Grenadines','Venezuela','British Virgin Islands','U.S. Virgin Islands','Vietnam','Vanuatu','Wallis & Futuna','Samoa','Kosovo','Yemen','Mayotte','South Africa','Zambia','Zimbabwe']
        
#         emoji_lists = list(zip(emoji_names,country_names))
#         global msg
#         for (x,y) in emoji_lists:
#             if reaction.message.id == msg:
#                 if reaction.emoji == x:
#                     if y not in [str(r.name) for r in ctx.guild.roles]:
#                         guild = ctx.guild
#                         role = await guild.create_role(name=y,colour=discord.Colour(0x000000))
#                         print("Created role " + str(y))
#                         role_id = role.id
#                         role_name = role.name

#                         con = sqlite3.connect('countries.db')
#                         cur = con.cursor()
#                         insert_query = f"INSERT INTO country(role_id,role_name) VALUES ('{role_id}','{role_name}')"
#                         cur.execute(insert_query)
#                         con.commit()
#                         con.close()
                    
#                     elif y in [str(r.name) for r in ctx.guild.roles]:
#                         find_role = discord.utils.get(member.guild.roles,name=y)
#                         await member.add_roles(find_role)

# @client.event
# async def on_reaction_add(reaction,member):
#     roles_info = []
#     con = sqlite3.connect('countries.db')
#     get_roles_query = "SELECT * FROM country"
#     cursor = con.cursor()
#     cursor.execute(get_roles_query)
#     roles_info.append(cursor.fetchall())

#     emoji_names = ['🇦🇨','🇦🇩','🇦🇪','🇦🇫','🇦🇬',
#                    '🇦🇮','🇦🇱','🇦🇲','🇦🇴','🇦🇶',
#                    '🇦🇷','🇦🇸','🇦🇹','🇦🇺','🇦🇼',
#                    '🇦🇽','🇦🇿','🇧🇦','🇧🇧','🇧🇩',
#                    '🇧🇪','🇧🇫','🇧🇬','🇧🇭','🇧🇮',
#                    '🇧🇯','🇧🇱','🇧🇲','🇧🇳','🇧🇴',
#                    '🇧🇶','🇧🇷','🇧🇸','🇧🇹','🇧🇻',
#                    '🇧🇼','🇧🇾','🇧🇿','🇨🇦','🇨🇨',
#                    '🇨🇩','🇨🇫','🇨🇬','🇨🇭','🇨🇮',
#                    '🇨🇰','🇨🇱','🇨🇲','🇨🇳','🇨🇴','🇨🇵',
#                    '🇨🇷','🇨🇺','🇨🇻','🇨🇼','🇨🇽',
#                    '🇨🇾','🇨🇿','🇩🇪','🇩🇬','🇩🇯','🇩🇰',
#                    '🇩🇲','🇩🇴','🇩🇿','🇪🇦','🇪🇨','🇪🇪',
#                    '🇪🇬','🇪🇭','🇪🇷','🇪🇸','🇪🇹','🇪🇺',
#                    '🇫🇮','🇫🇯','🇫🇰','🇫🇲','🇫🇴',
#                    '🇫🇷','🇬🇦','🇬🇧','🇬🇩','🇬🇪',
#                    '🇬🇫','🇬🇬','🇬🇭','🇬🇮','🇬🇱',
#                    '🇬🇲','🇬🇳','🇬🇵','🇬🇶','🇬🇷',
#                    '🇬🇸','🇬🇹','🇬🇺','🇬🇼','🇬🇾',
#                    '🇭🇰','🇭🇲','🇭🇳','🇭🇷','🇭🇹',
#                    '🇭🇺','🇮🇨','🇮🇩','🇮🇪','🇮🇱','🇮🇲',
#                    '🇮🇳','🇮🇴','🇮🇶','🇮🇷','🇮🇸',
#                    '🇮🇹','🇯🇪','🇯🇲','🇯🇴','🇯🇵',
#                    '🇰🇪','🇰🇬','🇰🇭','🇰🇮','🇰🇲',
#                    '🇰🇳','🇰🇵','🇰🇷','🇰🇼','🇰🇾',
#                    '🇰🇿','🇱🇦','🇱🇧','🇱🇨','🇱🇮',
#                    '🇱🇰','🇱🇷','🇱🇸','🇱🇹','🇱🇺',
#                    '🇱🇻','🇱🇾','🇲🇦','🇲🇨','🇲🇩',
#                    '🇲🇪','🇲🇫','🇲🇬','🇲🇭','🇲🇰',
#                    '🇲🇱','🇲🇲','🇲🇳','🇲🇴','🇲🇵','🇲🇶',
#                    '🇲🇷','🇲🇸','🇲🇹','🇲🇺','🇲🇻','🇲🇼',
#                    '🇲🇽','🇲🇾','🇲🇿','🇳🇦','🇳🇨','🇳🇪','🇳🇫',
#                    '🇳🇬','🇳🇮','🇳🇱','🇳🇴','🇳🇵',
#                    '🇳🇷','🇳🇺','🇳🇿','🇴🇲','🇵🇦','🇵🇪',
#                    '🇵🇫','🇵🇬','🇵🇭','🇵🇰','🇵🇱',
#                    '🇵🇲','🇵🇳','🇵🇷','🇵🇸','🇵🇹',
#                    '🇵🇼','🇵🇾','🇶🇦','🇷🇪','🇷🇴','🇷🇸',
#                    '🇷🇺','🇷🇼','🇸🇦','🇸🇧','🇸🇨','🇸🇩',
#                    '🇸🇪','🇸🇬','🇸🇭','🇸🇮','🇸🇯',
#                    '🇸🇰','🇸🇱','🇸🇲',
#                    '🇸🇳','🇸🇴',
#                    '🇸🇷','🇸🇸','🇸🇹','🇸🇻','🇸🇽','🇸🇾',
#                    '🇸🇿','🇹🇦','🇹🇨','🇹🇩','🇹🇫','🇹🇬','🇹🇭','🇹🇯','🇹🇰',
#                    '🇹🇱','🇹🇲','🇹🇳','🇹🇴',
#                    '🇹🇷','🇹🇹',
#                    '🇹🇻','🇹🇼','🇹🇿','🇺🇦','🇺🇬','🇺🇲','🇺🇳',
#                    '🇺🇸','🇺🇾','🇺🇿','🇻🇦','🇻🇨','🇻🇪',
#                    '🇻🇬','🇻🇮','🇻🇳','🇻🇺',
#                    '🇼🇫','🇼🇸','🇽🇰','🇾🇪','🇾🇹','🇿🇦','🇿🇲','🇿🇼']

#     country_names = ['Ascension Island','Andorra','United Arab Emirates','Afghanistan','Antigua & Barbuda',
#                      'Anguilla','Albania','Armenia','Angola','Antarctica',
#                      'Argentina','American Samoa','Austria','Australia','Aruba',
#                      'Åland Islands','Azerbaijan','Bosnia & Herzegovina','Barbados','Bangladesh',
#                      'Belgium','Burkina Faso','Bulgaria','Bahrain','Burundi',
#                      'Benin','St. Barthélemy','Bermuda','Brunei','Bolivia',
#                      'Caribbean Netherlands','Brazil','Bahamas','Bhutan','Bouvet Island',
#                      'Botswana','Belarus','Belize','Canada','Cocos(Keeling) Islands',
#                      'Congo - Kinshasa','Central African Republic','Congo - Brazzaville','Switzerland','Côte d’Ivoire',
#                      'Cook Islands','Chile','Cameroon','China','Colombia',
#                      'Clipperton Island','Costa Rica','Cuba','Cape Verde','Curaçao',
#                      'Christmas Island','Cyprus','Czechia','Germany','Diego Garcia','Djibouti','Denmark',
#                      'Dominica','Dominican Republic','Algeria','Ceuta & Melilla','Ecuador','Estonia',
#                      'Egypt','Western Sahara','Eritrea','Spain','Ethiopia',
#                      'European Union','Finland','Fiji','Falkland Islands','Micronesia','Faroe Islands',
#                      'France','Gabon','United Kingdom','Grenada','Georgia',
#                      'French Guiana','Guernsey','Ghana','Gibraltar','Greenland',
#                      'Gambia','Guinea','Guadeloupe','Equatorial','Greece',
#                      'South Georgia & South Sandwich Islands','Guatemala','Guam','Guinea-Bissau','Guyana',
#                      'Hong Kong SAR China','Heard & McDonald Islands','Honduras','Croatia','Haiti',
#                      'Hungary','Canary Islands','Indonesia','Ireland','Israel','Isle of Man',
#                      'India','British Indian Ocean Territory','Iraq','Iran','Iceland',
#                      'Italy','Jersey','Jamaica','Jordan','Japan',
#                      'Kenya','Kyrgyzstan','Cambodia','Kiribati','Comoros',
#                      'St. Kitts & Nevis','North Korea','South Korea','Kuwait',
#                      'Cayman Islands','Kazakhstan','Laos','Lebanon','St. Lucia','Liechtenstein',
#                      'Sri Lanka','Liberia','Lesotho','Lithuania','Luxembourg',
#                      'Latvia','Libya','Morocco','Monaco','Moldova',
#                      'Montenegro','St. Martin','Madagascar','Marshall Islands','North Macedonia',
#                      'Mali','Myanmar(Burma)','Mongolia','Macao Sar China','Northern Mariana Islands','Martinique',
#                      'Mauritania','Montserrat','Malta','Mauritius','Maldives','Malawi','Mexico','Malaysia','Mozambique','Namibia','New Caledonia','Niger','Norfolk Island','Nigeria','Nicaragua','Netherlands','Norway','Nepal','Nauru','Niue','New Zealand','Oman','Panama','Peru','French Polynesia','Papua New Guinea','Philippines','Pakistan','Poland','St. Pierre & Miquelon','Pitcairn Islands','Puerto Rico','Palestinian Territories','Portugal','Palau','Paraguay','Qatar','Réunion','Romania','Serbia','Russia','Rwanda','Saudi Arabia','Solomon Islands','Seychelles','Sudan','Sweden','Singapore','St. Helena','Slovenia','Svalbard & Jan Mayen','Slovakia','Sierra Leone','San Marino','Senegal','Somalia','Suriname','South Sudan','🇸🇹São Tomé & Príncipe','El Salvador','Sint Maarten','Syria','Eswatini','Tristan Da Cunha','Turks & Caicos Islands','Chad','French Southern Territories','Togo','Thailand','Tajikistan','Tokelau','Timor-Leste','Turkmenistan','Tunisia','Tonga','Turkey','Trinidad & Tobago','Tuvalu','Taiwan','Tanzania','Ukraine','Uganda','U.S. Outlying Islands','United Nations','United States','Uruguay','Uzbekistan','Vatican City','St. Vincent & Grenadines','Venezuela','British Virgin Islands','U.S. Virgin Islands','Vietnam','Vanuatu','Wallis & Futuna','Samoa','Kosovo','Yemen','Mayotte','South Africa','Zambia','Zimbabwe']
        
#     emoji_lists = list(zip(emoji_names,country_names))
#     for (a,b) in emoji_lists:
#         if a not in [y.id for y in member.roles]:
#             for (x,y) in emoji_lists:
#                 if reaction.emoji == x:
#                     find_role = discord.utils.get(member.guild.roles,name=y)
#                     await member.add_roles(find_role)
#     print("Added role " + str(find_role) + " to user.")


# @client.event
# async def on_raw_reaciton_remove(payload):
#     print("helo")
    # guild_id = payload.guild_id
    # guild = discord.utils.find(lambda g : g.id == guild_id,client.guilds)
    # emoji_lists = [("🇦🇩","Andorra"),("🇦🇪","United Arab Emirates") ,("🇦🇫","Afghanistan")]
    # for (a,b) in emoji_lists:
    #         if payload.emoji.name in a:
    #                 print("a")
    #         role = discord.utils.get(guild.roles,name=b)
    # if role is not None:
    #         member = discord.utils.find(lambda m : m.id == payload.user_id,guild.members)
    #         if member is not None:
    #                 await member.remove_roles(role)
    # emoji_lists = [("🇦🇩","Andorra"),("🇦🇪","United Arab Emirates") ,("🇦🇫","Afghanistan")]
    # for (t,z) in emoji_lists:
    #         if reaction.remove_reaction() in t:
    #                 print("hello")# await member.remove_roles(z)

