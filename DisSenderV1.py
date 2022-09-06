
import dearpygui.dearpygui as dpg
import discord

from dearpygui.dearpygui import add_font
import json
import requests



dpg.create_context()

with dpg.font_registry():
    with dpg.font(f'C:\\Windows\\Fonts\\Calibri.ttf', 13, default_font=True, id="Default font"):
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
dpg.bind_font("Default font")



def test(sender):
    slide = dpg.get_value(how)
    for i in range(int(slide)):
        id = dpg.get_value(ids)
        token1 = dpg.get_value(token)
        URL = f"https://discord.com/api/v9/channels/{id}/messages"

        value = dpg.get_value(text)
        r = requests.post(URL,data={"content": value},headers={"Authorization":f"Bot {token1}"})




    id = dpg.get_value(ids)
    dpg.get_value(token)
    URL = f"https://discord.com/api/v9/channels/{id}/messages"

    value = dpg.get_value(text)
    r = requests.post(URL,data={"content": value},headers={"Authorization":f"Bot {token1}"})


def remove(sender):
    id2 = dpg.get_value(ids1)
    token2 = dpg.get_value(token)
    URL2 = f"https://discord.com/api/v9/channels/{id2}"

    r2 = requests.delete(URL2,headers={"Authorization":f"Bot {token2}"})


def add(sender):
    slide = dpg.get_value(chanhow)
    for i in range(int(slide)):
        guil = dpg.get_value(idchan)
        token3 = dpg.get_value(token)
        addURL = f"https://discord.com/api/v9/guilds/{guil}/channels"
        name1 = dpg.get_value(addchannel)
        r3 = requests.post(addURL,json={"name": name1,"permission_overwrites" : [],"type": 0},headers={"Authorization":f"Bot {token3}"})



    guil = dpg.get_value(idchan)
    addURL = f"https://discord.com/api/v9/guilds/{guil}/channels"
    token3 = dpg.get_value(token)
    name1 = dpg.get_value(addchannel)
    r3 = requests.post(addURL,json={"name": name1,"permission_overwrites" : [],"type": 0},headers={"Authorization":f"Bot {token3}"})



def kick(sender):
    skickid = dpg.get_value(kickmem)
    memberid1 = dpg.get_value(memberid)
    token4 = dpg.get_value(token)
    kickURL = f"https://discord.com/api/v9/guilds/{skickid}/members/{memberid1}"

    kick = requests.delete(kickURL,headers={"Authorization":f"Bot {token4}"})


def servername(sender):
    servidname = dpg.get_value(servname)
    newname = dpg.get_value(name)
    token5 = dpg.get_value(token)
    nameURL = f"https://discord.com/api/v9/guilds/{servidname}"
    patchname = requests.patch(nameURL,json={"name": newname},headers={"Authorization":f"Bot {token5}"})
    print(patchname)




with dpg.window(label="DiscordSender", tag = "Primary Window"):
    token = dpg.add_input_text(label="Bot Token")

    dpg.add_text("Server Message Spam")

    ids = dpg.add_input_text(label="channel id for text")
    how = dpg.add_slider_int(label = "how message?")
    text = dpg.add_input_text(label="your text")
    dpg.add_button(label="send", callback = test)

    dpg.add_text("Server Channel Remove")
    ids1 = dpg.add_input_text(label="channel id for remove")
    dpg.add_button(label="remove channel", callback = remove)

    dpg.add_text("Server Channel Create")
    idchan = dpg.add_input_text(label="server id for create channel")
    addchannel = dpg.add_input_text(label="name channel for add")
    chanhow = dpg.add_slider_int(label = "how channels?")
    dpg.add_button(label="Add channel", callback=add)

    dpg.add_text("Member kick")
    kickmem = dpg.add_input_text(label="server id for kick")
    memberid = dpg.add_input_text(label="member id for kick")
    dpg.add_button(label="Kick member", callback = kick)

    dpg.add_text("Server Set Name")
    servname = dpg.add_input_text(label="server id for set name")
    name = dpg.add_input_text(label="new server name!")
    dpg.add_button(label="set name", callback = servername)





with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (51, 54, 61), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (87, 101, 242), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (104, 104, 104), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (64, 68, 76), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (62, 66, 74), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (64, 68, 76), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (44, 44, 44), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (44, 44, 44), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 20, category=dpg.mvThemeCat_Core)


dpg.bind_theme(global_theme)





dpg.create_viewport(title='DiscordSender', width=800, height=650)

dpg.set_viewport_small_icon("discordic.ico")
dpg.set_viewport_large_icon("discordic.ico")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
