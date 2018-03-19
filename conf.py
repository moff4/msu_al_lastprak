#!/usr/bin/env python3.6
#------------------------------------------------------------------------------
# That's configuration file
# U can change some values on ur own risk
#------------------------------------------------------------------------------

# max value of points user can get in one play
MAX_SCORE 	=	1000.0

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
# help message displayed on form (list of str)
Screen_help_msg = ["Ты управляешь <LEFT-OR-RIGHT> танком. Атакуй противника, чтобы набрать очки. \
Победит первый, кто наберет %s очков. "%(MAX_SCORE),
"Управление:",
"<- , -> - подвинуть танк влево/вправо",
" A , D  - увеличить, уменьшить угол наклона орудия",
" W , S  - увеличить, уменьшить мощность выстрела",
" Q , E  - Сменить снаряд",
" ПРОБЕЛ - выстрелить"
]
# str for left tank insterted in help-msg (str)
Screen_left_pos							=	"левым"
# str for rigth tank insterted in help-msg (str)
Screen_right_pos						=	"правым"
# text on stop button
stop_button_name						=	"Выход"
#------------------------------------------------------------------------------
#                                Connections
#------------------------------------------------------------------------------
# default host to advice user (str)
Connection_default_host					=	'127.0.0.1'
# default port to advice user (int)
Connection_default_port					=	9154
# timeout in seconds of waitng for peer (float or None)
Socket_listen_timeout					=	15

#------------------------------------------------------------------------------
#                                 Protocol
#------------------------------------------------------------------------------
# message for checking connection (bytes)
PING_MSG								=	b'msg-ping'
# message for closing connection (bytes)
CLOSE_MSG								=	b'msg-close'
# delay in seconds between ping requests and replies (float)
delay_ping								=	3.5

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
COMPRESSION_RATIO						=	2
#------------------------------------------------------------------------------
#                                 Basic Tank
#------------------------------------------------------------------------------
# max tank step for one button press (int)
Basic_tank_max_step						=	5
# color of the tank (str as "#??????") 
Basic_tank_color						=	'#00FF00'
# tank's size in pixels (float)
Basic_tank_size							=	30
#------------------------------------------------------------------------------
#                                Basic Misslie
#------------------------------------------------------------------------------
# Weight for speed of missle; the bigger weight - the bigger speed (float)
Missile_speed_weight					=	1.0
# length of missile traceback (int)
Missile_trace_length					=	5
# size of misslie in pixels (int)
Misslie_size							=	8
# color of the missile (str as "#??????")
Misslie_main_color						=	"#0000FF"
# color of the missile's trace (str as "#??????")
Misslie_trace_color						=	"#FF0000"
#------------------------------------------------------------------------------
#                                Basic Blow
#------------------------------------------------------------------------------
# max size of the blow in pixels (int)
Blow_max_size							=	50
# color of the blow's wave (str as "#??????")
Blow_color								=	"#FF0000"
# width of the blow's wave in pixels (int)
Blow_width								=	10
