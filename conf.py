#!/usr/bin/env python3.6
#------------------------------------------------------------------------------
# That's configuration file
# U can change some values on ur own risk
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#                                   GUI
#------------------------------------------------------------------------------
####################################################
###                    MAINMENU                  ###
####################################################

# Screen name on main menu (str)
MainMenu_ScreenName						=	'Tanks'
# Title on main menu (str)
MainMenu_logo							=	'TANKS'
# main background color (str as '#??????')
MainMenu_BackgroundColor				=	'#ccccff'
# window geometry (int,int,int,int)
MainMenu_width							=	250
MainMenu_height							=	225
MainMenu_left							=	600
MainMenu_top							=	250
# text on client radiobutton on main menu (str)
MainMenu_radio_text_1					=	'Клиент'
# text on server radiobutton on main menu (Str)
MainMenu_radio_text_2					=	'Сервер'
# text on start(continue) button on main menu (str) 
Start_button_name						=	'Продолжить'
# text on exit button on main menu (str) 
Exit_button_name						=	'Выход'
# text on label for host textbox on main menu (str) 
Label_host_name							=	'Хост:'
# text on label for port textbox on main menu (str) 
Label_port_name							=	'Порт:'

####################################################
###                     SCREEN                   ###
####################################################
# height of main game window (int)
Game_window_height						=	480
# width of main game window (int)
Game_window_width						=	1280
# Screen name on main menu (str)
Screen_ScreenName						=	'Tanks'
# main background color (str as '#??????')
Screen_BackgroundColor					=	'#ccccff'
# window geometry (int,int,int,int)
Screen_width							=	Game_window_width + 40
Screen_height							=	Game_window_height + 150
Screen_left								=	40
Screen_top								=	50
#------------------------------------------------------------------------------
#                                Connections
#------------------------------------------------------------------------------
# default host to advice user (str)
Connection_default_host					=	'127.0.0.1'
# default port to advice user (int)
Connection_default_port					=	9154
# timeout in seconds of waitng for peer (float ot None)
Socket_listen_timeout					=	15

#------------------------------------------------------------------------------
#                                 Protocol
#------------------------------------------------------------------------------
# message for checking connection (bytes)
PING_MSG								=	b'msg-ping'
# message for closing connection (bytes)
CLOSE_MSG								=	b'msg-close'
# delay in seconds between ping requests and replies (float)
delay_ping								=	5.5

#------------------------------------------------------------------------------
#                                   Engine
#------------------------------------------------------------------------------
# frames per seconds (float)
fps										=	10
# Pi - math const (float)
Pi										=	3.1415
# G - gravity const from physics (float)
G 										=	9.81
# for landscape generator
POLYNOMIAL_DEGREE						=	10
# Game_window_height / COMPRESSION_RATIO = max landscape height
COMPRESSION_RATIO						=	10
#------------------------------------------------------------------------------
#                                 Basic Tank
#------------------------------------------------------------------------------
# max tank step for one button press (int)
Basic_tank_max_step						=	5
# color of the tank (str as "#??????") 
Basic_tank_color						=	'#FF0000'
# tank's size in pixels (float)
Basic_tank_size							=	20
#------------------------------------------------------------------------------
#                                 Basic Missle
#------------------------------------------------------------------------------
# Weight for speed of missle; the bigger weight - the bigger speed (float)
Missle_speed_weight						=	1.0



