# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Sourced From Online Templates And Guides
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Thanks To: Google Search For This Template
# Modified: Pulse
# A diferencia de otros impresentables yo permito que este addon
# sea utilizado como mas se desee.
#------------------------------------------------------------


# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin , base64
# Plugin Info

ADDON_ID      = 'plugin.video.now_music'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

setting = xbmcaddon.Addon().getSetting
if setting('youtube_usar') == "0":  ##Reproducir con Youtube
    usa_duffyou = False
else:  ##Reproducir con Duff You
    usa_duffyou = True



YOUTUBE_CHANNEL_ID_1 = "PL_34_m4eTlaMSONcN_P4r5QFAWAwkngbX"
YOUTUBE_CHANNEL_ID_2 = "PL_34_m4eTlaOeNd6fP9MspKqh9ksDiNtm"
YOUTUBE_CHANNEL_ID_3 = "PLLK5DjpAskR68KFNnVgvq5mZHEXTQIyX7"
YOUTUBE_CHANNEL_ID_4 = "PL_34_m4eTlaOFcXryY7OFbYGtK5Y1JoIa"
YOUTUBE_CHANNEL_ID_5 = "PL_34_m4eTlaOtJMirQzXvOoAwdechWbhF"
YOUTUBE_CHANNEL_ID_6 = "PL_34_m4eTlaMf-42RHro2x2UVMHNEkLvD"
YOUTUBE_CHANNEL_ID_7 = "PL_34_m4eTlaN5Dj1kIzrJMX95HRBLqeQr"
YOUTUBE_CHANNEL_ID_8 = "PL1659BED42584319F"
YOUTUBE_CHANNEL_ID_9 = "PL8FA9A7569EBB5E4A"
YOUTUBE_CHANNEL_ID_10 = "PL_34_m4eTlaPzdgA9RG_BlIImsUwCVkzy"
YOUTUBE_CHANNEL_ID_11 = "PL_34_m4eTlaNHt6GM5dOnraJ2zdE4R2Z_"
YOUTUBE_CHANNEL_ID_12 = "PLO47Lo58fyaJTRmPSH3eIx4R92WngXEeu"
YOUTUBE_CHANNEL_ID_13 = "PLBB7D0AF873F8FAEA" 
YOUTUBE_CHANNEL_ID_14 = "PL912C2772F94A73F9" 
YOUTUBE_CHANNEL_ID_15 = "PL_IGfDhmSGBMtrZrP0X440vgv5iBRfhy4"
YOUTUBE_CHANNEL_ID_16 = "PL6CDBDD2A3C0D55A5"
YOUTUBE_CHANNEL_ID_17 = "PLziBTZqySBRFOFOwbSuPn4GtockoGot7k" 
YOUTUBE_CHANNEL_ID_18 = "PLDouWbMQEftHiTge92lMQFgbNVUCBlP8E"
YOUTUBE_CHANNEL_ID_19 = "PLDouWbMQEftFRzud9bJO0Yg03R6TaJoL3"
YOUTUBE_CHANNEL_ID_20 = "PLDouWbMQEftHqrKjdu7cFSACIudT2n5Il" 
YOUTUBE_CHANNEL_ID_21 = "PL_34_m4eTlaNLsqqXEC3D-QPlMpgGqrFy"
YOUTUBE_CHANNEL_ID_22 = "PL6A8E66F870D64825"
YOUTUBE_CHANNEL_ID_23 = "PL_34_m4eTlaMDLrSesIGNfArzdqbV9PtO" 
YOUTUBE_CHANNEL_ID_24 = "PL_34_m4eTlaOcF4HOTM5_u7WEz5UOknPc"
YOUTUBE_CHANNEL_ID_25 = "PL_34_m4eTlaP6n2tYDBKamuvoQDo89a97"
YOUTUBE_CHANNEL_ID_26 = "PL_34_m4eTlaOoOkgbOgS93OFQ9QxTPJYP"
YOUTUBE_CHANNEL_ID_27 = "PL_34_m4eTlaMBcJhd_fEj-QBpb8P89F28" 
YOUTUBE_CHANNEL_ID_28 = "PL_34_m4eTlaN1pIJXJpatZyWCnQgPr_nU"
YOUTUBE_CHANNEL_ID_29 = "PL_34_m4eTlaOh7AX4GJRnnxKgJ5n9_V-M"
YOUTUBE_CHANNEL_ID_30 = "PL_34_m4eTlaMnTgbpMYRKfReUqZw1LRuJ"
YOUTUBE_CHANNEL_ID_31 = "PLuDr0us3k-BveJdm67f8SlDt87aRtyZ2r"
YOUTUBE_CHANNEL_ID_32 = "PL_34_m4eTlaMMi2E-nHwk4OdRi3OJQ78b"
YOUTUBE_CHANNEL_ID_33 = "PL_34_m4eTlaMO4Mz_dWge1XC9K2uhXThR" 
YOUTUBE_CHANNEL_ID_34 = "PL_34_m4eTlaPl5bRHTsf1kogkcS80LiEi"
YOUTUBE_CHANNEL_ID_35 = "PL1F0D80E99F7850E5"
YOUTUBE_CHANNEL_ID_36 = "PL_34_m4eTlaOryUpz8B44gf1tyxsyEJL1"
YOUTUBE_CHANNEL_ID_37 = "PLDouWbMQEftGj0O3468TrleWCTMTJrS20"
YOUTUBE_CHANNEL_ID_38 = "PLDouWbMQEftGzuFV8LqaBidN4Nr3WGWLk" 
YOUTUBE_CHANNEL_ID_39 = "PL_34_m4eTlaPcjuqnypKfhVVpHKmT4yxH"
YOUTUBE_CHANNEL_ID_40 = "PL_34_m4eTlaOg18XvgjqGTvFtX26QqIui"
YOUTUBE_CHANNEL_ID_41 = "PL_34_m4eTlaOakp50tDGnTQ2fwt4U8ewy"
YOUTUBE_CHANNEL_ID_42 = "PL_34_m4eTlaM_-9ciPXJA33ncF322YWA5"
YOUTUBE_CHANNEL_ID_43 = "PL_34_m4eTlaPSdTUlEYBLM4ewrck1RDvh" 
YOUTUBE_CHANNEL_ID_44 = "PLwNBYqY3GP2f9DZr6XdDgW8VwyPEX9bm7"
YOUTUBE_CHANNEL_ID_45 = "PLMw8cPF2uPc6eneUtoFamsrvGGZlF2uqL"
YOUTUBE_CHANNEL_ID_46 = "PLDouWbMQEftEHpZkhMpIwlWz1iE96HbQq"
YOUTUBE_CHANNEL_ID_47 = "PLDouWbMQEftFtfaMjEM-9IjipNjw7qJ5W"
YOUTUBE_CHANNEL_ID_48 = "PLDouWbMQEftH195uyZ0SlBVSznM61I8J3" 
YOUTUBE_CHANNEL_ID_49 = "PLDouWbMQEftHe0rKzAJPb7MGltCPtFxNs"
YOUTUBE_CHANNEL_ID_50 = "PLgK4BjZPsT825ISNA4dWqsnUuUQEfHZEu"
YOUTUBE_CHANNEL_ID_51 = "PLDouWbMQEftHJSvaRvBzvFZ4S34kucnwl"
YOUTUBE_CHANNEL_ID_52 = "PLDouWbMQEftF5HyM_lheKxX38sRZdcdfR"
YOUTUBE_CHANNEL_ID_53 = "PLDouWbMQEftEasB5KoU8faJqOQVCOq810" 
YOUTUBE_CHANNEL_ID_54 = "PLDouWbMQEftEcdNjhvM5YeVvXSl9nxOaU"
YOUTUBE_CHANNEL_ID_55 = "PL8Mowahw6-au9odO_rwNnWcxgdTdNVr_3"
YOUTUBE_CHANNEL_ID_56 = "PLDouWbMQEftF-RQMo2YsYzrR_ZByg947D"
YOUTUBE_CHANNEL_ID_57 = "PLDouWbMQEftEcdNjhvM5YeVvXSl9nxOaU"
YOUTUBE_CHANNEL_ID_58 = "PLDouWbMQEftEDrxxz3VoXIEfiQbYeOJ2l" 
YOUTUBE_CHANNEL_ID_59 = "PLDouWbMQEftEAJUcUYopDaqCbcmMIlIMl"
YOUTUBE_CHANNEL_ID_60 = "PLDouWbMQEftHqvpVkKeBiPszLECporRWe"
YOUTUBE_CHANNEL_ID_61 = "PLDouWbMQEftEvDn_oWxYCOOcbLk86TJTV"
YOUTUBE_CHANNEL_ID_62 = "PLDouWbMQEftGij9_IK8pIwRZ9wf0rcYc9"
YOUTUBE_CHANNEL_ID_63 = "PLDouWbMQEftFRdgKkRkFOvCi69YxICjzI" 
YOUTUBE_CHANNEL_ID_64 = "PLDouWbMQEftEEeKB6GcLaDQbypvob4e10"
YOUTUBE_CHANNEL_ID_65 = "PLDouWbMQEftHfSufbFaP1N5UvSZwuBQxj"
YOUTUBE_CHANNEL_ID_66 = "PLDouWbMQEftEXRa9q30waTahj7mpRrttU"
YOUTUBE_CHANNEL_ID_67 = "PLDouWbMQEftEylNuZbUaDdnjEVb4K8NXk"
YOUTUBE_CHANNEL_ID_68 = "PLDouWbMQEftFPAozxK35cermZl8JmEm6w" 
YOUTUBE_CHANNEL_ID_69 = "PLDouWbMQEftH05DjkYFT35ubDtJ9-EDAQ"
YOUTUBE_CHANNEL_ID_70 = "PLDouWbMQEftFLmCbJNnxBqo925x89tJci"
YOUTUBE_CHANNEL_ID_71 = "PLDouWbMQEftE3cvxvmmZbmb5LHFSqquC2"
YOUTUBE_CHANNEL_ID_72 = "PLDouWbMQEftHVApkssY45f20pBKQkubda"
YOUTUBE_CHANNEL_ID_73 = "PLDouWbMQEftE3qNQFpHbwtds_fClgrosx" 
YOUTUBE_CHANNEL_ID_74 = "PLDouWbMQEftHbsC27ysUWGw4OxnKwgmSI"
YOUTUBE_CHANNEL_ID_75 = "PLDouWbMQEftGxi1_JHCEMj0Mg6xu8ofTS"
YOUTUBE_CHANNEL_ID_76 = "PLDouWbMQEftGppOc9H3k4OblZt7AkFJIe"
YOUTUBE_CHANNEL_ID_77 = "PLDouWbMQEftFwkKFJg_dqrNZmViR_5Vpw"
YOUTUBE_CHANNEL_ID_78 = "PLDouWbMQEftGm-SYQFcZgSkl5Xsoi6ec3" 
YOUTUBE_CHANNEL_ID_79 = "PLDouWbMQEftG7H9iL5_e-05Qln6eOHzhJ"
YOUTUBE_CHANNEL_ID_80 = "PLDouWbMQEftFo66cP_Slk1oCoVZRVPQae"
YOUTUBE_CHANNEL_ID_81 = "PLDouWbMQEftGIy9zgfcIK_T0Qt0J_VJ5C"
YOUTUBE_CHANNEL_ID_82 = "PLDouWbMQEftHsFyHSBua-RZLFsx--Cu4U"
YOUTUBE_CHANNEL_ID_83 = "PLDouWbMQEftFfvSiP-qJnSRplBPtP9V0b" 
YOUTUBE_CHANNEL_ID_84 = "PLDouWbMQEftFtXgRrax8PJPPC1gdQIJ70"
YOUTUBE_CHANNEL_ID_85 = "PLDouWbMQEftGVhou1WEt7puGQOB7Ieiqw"
YOUTUBE_CHANNEL_ID_86 = "PLDouWbMQEftGnfnnc1hgtKo47JFFZO43A"
YOUTUBE_CHANNEL_ID_87 = "PLDouWbMQEftFoFXgF3j3d-2ViUyC8KXxV" 
YOUTUBE_CHANNEL_ID_88 = "PLDouWbMQEftEpPsQuisDX830NEqIg6pLB"
YOUTUBE_CHANNEL_ID_89 = "PLDouWbMQEftE9awijXpVSoSbRho30vX8Z"
YOUTUBE_CHANNEL_ID_90 = "PL1CAE497B646AD1A6"
YOUTUBE_CHANNEL_ID_91 = "PL729690CF3DC4038B"
YOUTUBE_CHANNEL_ID_92 = "PL91AE51E5AD495C42" 
YOUTUBE_CHANNEL_ID_93 = "PL395E7954B52B4822"
YOUTUBE_CHANNEL_ID_94 = "PLoDgQlTbBQzbdvhDlUw9NY4IW-RgpZ62E"
YOUTUBE_CHANNEL_ID_95 = "PL_34_m4eTlaP1Oisln8FWSQ-uJfb-jJfO"
YOUTUBE_CHANNEL_ID_96 = "PL_34_m4eTlaN0b1Wntb0io2m_j0Bbe1Id" 
YOUTUBE_CHANNEL_ID_97 = "PLFHCz0ifDWM1F-kNF9Kpo_WMniLJSDJYG"
YOUTUBE_CHANNEL_ID_98 = "PL_34_m4eTlaNQBMQYxfxQLN7eUkIKP66y"
YOUTUBE_CHANNEL_ID_99 = "PLQa1P8Aw9Jz9u3H6qDnSMz91HFK05u8Qi" 
YOUTUBE_CHANNEL_ID_100 = "PLCyMOjFkWxz0x7YHwWgdkqCB4BZSOYlVu"
YOUTUBE_CHANNEL_ID_101 = "PL_34_m4eTlaNLWS-34FVBlr8ZnlTUFkiV"
YOUTUBE_CHANNEL_ID_102 = "PL_34_m4eTlaMs7Q4Imtz199e2K4agqwyP"
YOUTUBE_CHANNEL_ID_103 = "PL_34_m4eTlaNh63gxFpUwwAROXj5V3AX8" 
YOUTUBE_CHANNEL_ID_104 = "PL_34_m4eTlaMFVmKb3lBxVKMWkGXUKG9g"
YOUTUBE_CHANNEL_ID_105 = "PL_34_m4eTlaPXh3wyeVKGJJvjJtZ-kJXY"
YOUTUBE_CHANNEL_ID_106 = "PLf8Oo47thU_O5ZvVPjAymfbAHZt3Tgr9m"
YOUTUBE_CHANNEL_ID_107 = "PLUSRfoOcUe4aJ_afJI6Iw_d-IMx16iwnH"
YOUTUBE_CHANNEL_ID_108 = "PLUSRfoOcUe4YctgFFjWQqhbndPAX0eJ8c" 
YOUTUBE_CHANNEL_ID_109 = "PLCJyoxQW5ieKzjL8MH3qyvR1Kf6jT2_Rn"
YOUTUBE_CHANNEL_ID_110 = "PLF73D80737572C687"
YOUTUBE_CHANNEL_ID_111 = "PL_34_m4eTlaNZnmJKJqLfslC2oW3kNKWK"
YOUTUBE_CHANNEL_ID_112 = "PLft313ngIElbbRJBRLtnP59MUOuo24kGr"
YOUTUBE_CHANNEL_ID_113 = "PLHHnmhLfwSsaZzrbBUH_N0WB6cZFFeJ41" 
YOUTUBE_CHANNEL_ID_114 = "PL_34_m4eTlaP5cyIG-2hUcqF2bZxHgZlZ"
YOUTUBE_CHANNEL_ID_115 = "PL_34_m4eTlaMgClOUihGU5EKM0md93FCN"
YOUTUBE_CHANNEL_ID_116 = "PL_34_m4eTlaOrcFRHD9mG4zUilcXQS8uB"
YOUTUBE_CHANNEL_ID_117 = "PLsdPA0A_fKLmuHNuafb76kecjHqeGoBLs"
YOUTUBE_CHANNEL_ID_118 = "PLF0A9B9128F4397BD" 
YOUTUBE_CHANNEL_ID_119 = "PL_34_m4eTlaPLkaa4gLSJsWm86Z0H8i_U"
YOUTUBE_CHANNEL_ID_120 = "PL_34_m4eTlaO64lWBQeC7xfmlA9uKvS4G"
YOUTUBE_CHANNEL_ID_121 = "PLXAN7tYrZq7drpFeMFFn7CNzkF-FUVIBh"
YOUTUBE_CHANNEL_ID_122 = "PLUSRfoOcUe4ZHOPA0YgBcbwAVkJQ52HH_"
YOUTUBE_CHANNEL_ID_123 = "PLBBC3BAC472A1020F" 
YOUTUBE_CHANNEL_ID_124 = "PLnknRVaLM8J_02U2zaSzX_9wvfmctT1Xe"
YOUTUBE_CHANNEL_ID_125 = "PLEE1730DB6C1BDCB4"
YOUTUBE_CHANNEL_ID_126 = "PL_34_m4eTlaO8Wj-65W7BioLh50i_4Mzs"
YOUTUBE_CHANNEL_ID_127 = "PL_34_m4eTlaMA1WFX92nvR5NK1Z4dc42M"
YOUTUBE_CHANNEL_ID_128 = "PLfXJnC0pregyWgUZzmnzasnwxhCZw0uqK" 
YOUTUBE_CHANNEL_ID_129 = "PLflvWSBDC77jVrR_6MzUHBsITaIxn4jZ8"
YOUTUBE_CHANNEL_ID_130 = "PLKfO_IEZedrhfX21ih0rSRzLKPMFnsPcx"
YOUTUBE_CHANNEL_ID_131 = "PLC9uHuoWKsDwFs_bLjU1Xf9kK032tIukr"
YOUTUBE_CHANNEL_ID_132 = "PLsdPA0A_fKLlogBKy9a0UsGUngUm2Nu7O"
YOUTUBE_CHANNEL_ID_133 = "PL_34_m4eTlaMExaWbVfv24i5O5Q5ZBZXU"
YOUTUBE_CHANNEL_ID_134 = "PL_34_m4eTlaNf6TSaM9IfLd13R1lKaoYd"
YOUTUBE_CHANNEL_ID_135 = "PL_34_m4eTlaMYv6z-uHidbtQ199xd1EK1"
YOUTUBE_CHANNEL_ID_136 = "PL_34_m4eTlaPnat1HtGrigGFXywxRscUK"
YOUTUBE_CHANNEL_ID_137 = "PL_34_m4eTlaMnlJjHHCOyEK0jDM7_dHQ5"
YOUTUBE_CHANNEL_ID_138 = "PL-PXKb5jSjwZT2QzeJCIlYSqs0cZvy808"
YOUTUBE_CHANNEL_ID_139 = "UCfJPtULqanZ3K7trqtupvtQ"
YOUTUBE_CHANNEL_ID_140 = "PLLQvN69uicxzOl5c_mdEQ5ri4bEtblnPz"
YOUTUBE_CHANNEL_ID_141 = "PL_34_m4eTlaNMHpdUrP4JatalX_KatG0y"
YOUTUBE_CHANNEL_ID_142 = "PL_34_m4eTlaN6hX-sJcrJCJvRL4pSrPx0"
YOUTUBE_CHANNEL_ID_143 = "PL_34_m4eTlaPorC89EUOQxwhXeZxd-Hc7"
YOUTUBE_CHANNEL_ID_144 = "PL_34_m4eTlaMaiHbxdGrxy8AdgHtUezSO"
YOUTUBE_CHANNEL_ID_145 = "PL_34_m4eTlaMnl1WrUx3FjpJUlCWpApmR"
YOUTUBE_CHANNEL_ID_146 = "PL_34_m4eTlaPc_CPB-hrNUzBQF4bFOHWd"
YOUTUBE_CHANNEL_ID_147 = "PL_34_m4eTlaP8vMmdKKQpo4pm0efcwkxc"
YOUTUBE_CHANNEL_ID_148 = "PL1h8do6DyqVNYJXvKZWQO1IHKsg4Q7WMr"
YOUTUBE_CHANNEL_ID_149 = "PL_34_m4eTlaNtpSmdO1uPMFcVmtiKVcDl"
YOUTUBE_CHANNEL_ID_150 = "PL_34_m4eTlaMCpwncwUniCT_BbmDf3YGH"
YOUTUBE_CHANNEL_ID_151 = "PL7e7DXIcZhngq9s9w-DHtjasnDTY0GU9U"
YOUTUBE_CHANNEL_ID_152 = "PL7e7DXIcZhngq9s9w-DHtjasnDTY0GU9U"
YOUTUBE_CHANNEL_ID_153 = "PL7e7DXIcZhnhRWjyE0FZtj6fr5GEiq-oP"
YOUTUBE_CHANNEL_ID_154 = "PL_34_m4eTlaOke2S7jdu6iOhjx855Tflx"
YOUTUBE_CHANNEL_ID_155 = "PL_34_m4eTlaN8soNfVssZTAK-Ih8tSAZK"
YOUTUBE_CHANNEL_ID_156 = "PL_34_m4eTlaOtMwjz_WhS4HDWbIWY4Q5h"
YOUTUBE_CHANNEL_ID_157 = "PL_34_m4eTlaMHeUxzgeE_l2GKSInf3T_M"
YOUTUBE_CHANNEL_ID_158 = "PL_34_m4eTlaNCJ_rpWPq12Hx5Hq68YTMB"
YOUTUBE_CHANNEL_ID_159 = "PL_34_m4eTlaP_AUskfwanaNWPY8LdTDgo"
YOUTUBE_CHANNEL_ID_160 = "PL_34_m4eTlaNFNaZJX9MbbrObgT2f8xa0"
YOUTUBE_CHANNEL_ID_161 = "PL8yxY79U8QJVqQn0mb8_OUh1fvk9CjpP4"
YOUTUBE_CHANNEL_ID_162 = "PLf10VA90zVApIi9KuZBIOH3wE3KBciP3e"
YOUTUBE_CHANNEL_ID_163 = "PLhV4RKTkP5JS2cTb99uURQ6NhKSY4f4Cg"
YOUTUBE_CHANNEL_ID_164 = "PLcDjsIAbpJ9qpn3x39B_xTi0Dd0ZUjpy8"
YOUTUBE_CHANNEL_ID_165 = "PLbiwIhwYwKHpPgKvZaEfGK4PB7tLLmnyi"
YOUTUBE_CHANNEL_ID_166 = "PLbiwIhwYwKHpxuKou_C9N1KS6wg0X2jvA"
YOUTUBE_CHANNEL_ID_167 = "PLbiwIhwYwKHo224FvO6owwoJYBRL38OMY"
YOUTUBE_CHANNEL_ID_168 = "PLW_NpxKH1uD8mIhV4JmXVhuOQYZsfFhjb"
YOUTUBE_CHANNEL_ID_169 = "PLhV4RKTkP5JSPcckgTT35sDIFiZJi3sCj"
YOUTUBE_CHANNEL_ID_170 = "PLW_NpxKH1uD9iy1fQ0OREWwLDg8NLtsx-"
YOUTUBE_CHANNEL_ID_171 = "PLeHFVBju_a-m33jRcl9Wob78E-i-Hsryh"
YOUTUBE_CHANNEL_ID_172 = "PLf10VA90zVApIwYqr2heWOyJwWYpTjm0r"









if usa_duffyou:  ##Usamos plugin Duff You
    YOUTUBE_search = "plugin://plugin.video.duffyou/?eydhY3Rpb24nOiAnb2lPTzAwT28nLCAnZmFuYXJ0JzogJ0M6XFxVc2Vyc1xcZGFyaW9cXEFwcERhdGFcXFJvYW1pbmdcXEtvZGlcXGFkZG9uc1xccGx1Z2luLnZpZGVvLmR1ZmZ5b3VcXGZhbmFydC5qcGcnLCAnaWNvbic6ICdDOlxcVXNlcnNcXGRhcmlvXFxBcHBEYXRhXFxSb2FtaW5nXFxLb2RpXFxhZGRvbnNcXHBsdWdpbi52aWRlby5kdWZmeW91XFxyZXNvdXJjZXNcXG1lZGlhXFxuZXdfc2VhcmNoLnBuZycsICdsYWJlbCc6IHUnW0JdTnVldmEgQlx4ZmFzcXVlZGFbL0JdJywgJ3BhZ2UnOiAxLCAncGxvdCc6IHUnW0JdQnVzY2FyWy9CXVtDUl1bQ1JdQnVzY2EgdW4gdmlkZW8sIHVuIGRpcmVjdG8sIHVuYSBwbGF5bGlzdCBvIHVuIGNhbmFsLicsICdxdWVyeSc6IFRydWUsICd0aXBvJzogJ3ZpZGVvJ30%3d"
else:
    #YOUTUBE_search = "plugin://plugin.video.youtube/kodion/search/list/" 
    YOUTUBE_search = "plugin://plugin.video.youtube/kodion/search/input/"


def playlist_duffyou(id_playlist): 

    duffyou = "eydhY3Rpb24nOiAnaW8xaTFJMScsICdmYW5hcnQnOiAnJywgJ2ljb24nOiAnJywgJ2lkJzogJ01JLUlELVBMQVlMSVNUJywgJ2xhYmVsJzogJycsICdwYWdlJzogMSwgJ3Bsb3QnOiAiIiwgJ3F1ZXJ5JzogdSIiLCAndGh1bWInOiAnJywgJ3RpcG8nOiAncGxheWxpc3QnfQ=="

    if usa_duffyou:  ##Usamos plugin Duff You
        reemplaza = base64.b64decode(duffyou.encode('utf-8')).decode('utf-8').replace("MI-ID-PLAYLIST" , id_playlist)
        miLista = "plugin://plugin.video.duffyou/?" + base64.b64encode(reemplaza.encode('utf-8')).decode('utf-8')
    else:  ##Usamos Youtube
        miLista = "plugin://plugin.video.youtube/playlist/"+id_playlist+"/"
    
    return(miLista)

def addDir(title, url, thumbnail,folder):
    url2 = url.replace('plugin://plugin.video.youtube/playlist/"+','').replace('+"/','')
    url3 = playlist_duffyou(url2)
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)


if __name__ == '__main__':
    addDir(title="NOW – 80s Alternative (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_172+"/",thumbnail="https://tinyurl.com/3wtdb7hy",folder=True )    
    addDir(title="NOW That’s What I Call Legendary (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_171+"/",thumbnail="https://tinyurl.com/4r5vjun3",folder=True )
    addDir(title="NOW That’s What I Call Eurovision Song Contest (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_170+"/",thumbnail="https://tinyurl.com/3edccy36",folder=True )
    addDir(title="NOW THAT'S WHAT I CALL MUSIC! 114 (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_169+"/",thumbnail="https://tinyurl.com/3vt5z4yh",folder=True )
    addDir(title="NOW That's What I Call Massive Hits & #1s (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_168+"/",thumbnail="https://tinyurl.com/3esmhu88",folder=True )
    addDir(title="Now That’s What I Call 60s Pop (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_167+"/",thumbnail="https://tinyurl.com/yf9thw28",folder=True )
    addDir(title="Now Dance - The 80s Dance (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_166+"/",thumbnail="https://tinyurl.com/m9ubm32d",folder=True )
    addDir(title="Now that’s what I call a love song (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_165+"/",thumbnail="https://tinyurl.com/3kntnv37",folder=True )
    addDir(title="Now that's what I call a massive 80's Party (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_164+"/",thumbnail="https://tinyurl.com/39puazw2",folder=True )
    addDir(title="Now 113 (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_163+"/",thumbnail="https://tinyurl.com/2pvtzwf3",folder=True )
    addDir(title="Now Total Eclipse Of The Heart: Power Ballads (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_162+"/",thumbnail="https://tinyurl.com/ywkn6u6m",folder=True)
    addDir(title="Now 112 (Fanlist)",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_161+"/",thumbnail="https://tinyurl.com/4ejxsjn3",folder=True )
    addDir(title="Now Pride Playlist ",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_160+"/",thumbnail="https://bit.ly/3JmKPw1",folder=True )
    addDir(title="Now 111 ",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_159+"/",thumbnail="https://i.imgur.com/qIFlzD0.jpg",folder=True )
    addDir(title="Now 110 ",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_158+"/",thumbnail="https://i.imgur.com/yGWkEhA.jpg",folder=True )
    addDir(title="Now 109 ",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_157+"/",thumbnail="https://i.imgur.com/POCT55l.jpg",folder=True )
    addDir(title="NOW Live Forever: The Anthems",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_156+"/",thumbnail="https://i.imgur.com/ry2sJwP.jpg",folder=True )
    addDir(title="Now 108 ",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_155+"/",thumbnail="https://i.imgur.com/CO0f6kJ.jpg",folder=True )
    addDir(title="Now 107 ",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_154+"/",thumbnail="https://i.imgur.com/pRr2qWn.jpg",folder=True )
    addDir(title="Now106",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_150+"/",thumbnail="https://i.imgur.com/Xd1FeIr.jpg",folder=True)
    addDir(title="Now105",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_149+"/",thumbnail="https://i.imgur.com/fiZKrsL.jpg",folder=True)
    addDir(title="Now104",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_153+"/",thumbnail="https://i.imgur.com/BzTusPS.jpg",folder=True)
    addDir(title="Now103",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_152+"/",thumbnail="https://i.imgur.com/5TuWg6D.jpg",folder=True)
    addDir(title="Now102",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_151+"/",thumbnail="https://i.imgur.com/Byaz2GL.jpg",folder=True)
    addDir(title="Now101",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_147+"/",thumbnail="https://i.imgur.com/ehSuKWi.jpg",folder=True)
    addDir(title="Now100",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_146+"/",thumbnail="https://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/2018/04/now_100_stadium300dp.jpg",folder=True)
    addDir(title="Now99",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_145+"/",thumbnail="https://i.imgur.com/0KBOzBR.jpg",folder=True)
    addDir(title="Now98",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_144+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/2017/10/FINAL-now98ski1300dpi.png",folder=True)
    addDir(title="Now97",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_143+"/",thumbnail="https://i.imgur.com/U4UoX1G.jpg",folder=True)
    addDir(title="NowSummerHits",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_142+"/",thumbnail="https://i.imgur.com/Ft2b0Py.jpg",folder=True)
    addDir(title="Now96",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_141+"/",thumbnail="https://i.imgur.com/Kimgitd.jpg",folder=True)
    addDir(title="NowLevantateyCardenas2017",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_140+"/",thumbnail="http://i.imgur.com/dTndlqq.png",folder=True)
    addDir(title="NowKaraokeEd.España",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_139+"/",thumbnail="http://i.imgur.com/1Jieu64.png",folder=True)
    addDir(title="NowLosExitosDelAño2016",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_138+"/",thumbnail="http://www.fonodisco.es/227689-thickbox_default/now-2016-varios-2-cds-cd-.jpg",folder=True)
    addDir(title="Now95",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_133+"/",thumbnail="https://i.imgur.com/uLjPLw4.jpg",folder=True)
    addDir(title="Now94",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_130+"/",thumbnail="https://i.imgur.com/jRxNnCI.jpg",folder=True)
    addDir(title="Now93",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",thumbnail="http://www.officialcharts.com/media/650017/now-93-artwork.png?width=488.07157057654075&height=500",folder=True)
    addDir(title="Now92",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/20150923101439/now92GROTTO_HR-1024x1024.jpg",folder=True)
    addDir(title="Now91",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/20150611093502/now-91-CYMK-FINAL-HR-1024x1024.jpg",folder=True)
    addDir(title="Now90",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",thumbnail="https://i.imgur.com/z3TepVV.jpg",folder=True)
    addDir(title="Now89",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOW-89-Final-Artwork-1024x1024.jpg",folder=True)
    addDir(title="Now88",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",thumbnail="https://i.imgur.com/6p9luo4.jpg",folder=True)
    addDir(title="Now87",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/now_87_EGG_final-1024x1024.jpg",folder=True)
    addDir(title="Now86",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/now86NEW_FINAL-1024x1024.jpg",folder=True)
    addDir(title="Now85",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Pack-shot2-1024x1024.jpg",folder=True)
    addDir(title="Now84",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",thumbnail="http://ecx.images-amazon.com/images/I/81087xfVSDL._SL1500_.jpg",folder=True)
    addDir(title="Now83",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",thumbnail="https://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/2016/08/NOW_83.jpg",folder=True)
    addDir(title="Now82",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",thumbnail="http://tshop.r10s.com/3dc/0b1/5e1c/4b6d/20d8/3df1/8455/112ce49d9a005056b75a2f.jpg",folder=True)
    addDir(title="Now81",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/now-81.jpg",folder=True)
    addDir(title="Now80",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",thumbnail="https://i.imgur.com/UtULnWY.jpg",folder=True)
    addDir(title="Now79",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOW79_F_flop_CYMK-1024x1024.jpg",folder=True)
    addDir(title="Now78",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",thumbnail="https://i.imgur.com/EkKlSqj.jpg",folder=True)
    addDir(title="Now77",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/N77snowboardYEL-1024x1024.jpg",folder=True)
    addDir(title="Now76",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now76HR-1024x1024.jpg",folder=True)
    addDir(title="Now75",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",thumbnail="https://i.imgur.com/qcRWhka.jpg",folder=True)
    addDir(title="Now74",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/now74Sflakes_final-1024x1024.jpg",folder=True)
    addDir(title="Now73",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/N73_FINAL_HR-1024x1024.jpg",folder=True)
    addDir(title="Now72",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-72-1024x1024.jpg",folder=True)
    addDir(title="Now71",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-71-1024x1024.jpg",folder=True)
    addDir(title="Now70",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-70-1024x1024.jpg",folder=True)
    addDir(title="Now69",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-69-1024x1024.jpg",folder=True)
    addDir(title="Now68",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/61tRYeXQQCL.jpg",folder=True)
    addDir(title="Now67",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-67-1024x1024.jpg",folder=True)
    addDir(title="Now66",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-66-1024x1024.jpg",folder=True)
    addDir(title="Now65",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-65-1024x1024.jpg",folder=True)
    addDir(title="Now64",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-64-1024x1024.jpg",folder=True)
    addDir(title="Now63",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",thumbnail="https://i.imgur.com/cITBhw1.jpg",folder=True)
    addDir(title="Now62",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-62-1024x1024.jpg",folder=True)
    addDir(title="Now61",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-61.jpg",folder=True)
    addDir(title="Now60",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-60-1024x1024.jpg",folder=True)
    addDir(title="Now59",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-59-1024x1024.jpg",folder=True)
    addDir(title="Now58",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-58-1024x1024.jpg",folder=True)
    addDir(title="Now57",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",thumbnail="https://i.imgur.com/zjadg6e.jpg",folder=True)
    addDir(title="Now56",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",thumbnail="http://ecx.images-amazon.com/images/I/91QvXvWXU1L._SY355_.jpg",folder=True)
    addDir(title="Now55",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",thumbnail="http://ecx.images-amazon.com/images/I/71kFlRrz8aL._SX355_.jpg",folder=True)
    addDir(title="Now54",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",thumbnail="https://i.imgur.com/aissNwR.jpg",folder=True)
    addDir(title="Now53",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",thumbnail="https://i.imgur.com/kXUKGNh.jpg",folder=True)
    addDir(title="Now52",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",thumbnail="https://i.imgur.com/TFuAtCt.jpg",folder=True)
    addDir(title="Now51",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/81%2Bh5v6hPrL._SL1500_.jpg",folder=True)
    addDir(title="Now50",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",thumbnail="https://i.imgur.com/gGxxr3y.jpg",folder=True)
    addDir(title="Now49",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",thumbnail="https://i.imgur.com/FzxeVNA.jpg",folder=True)
    addDir(title="Now48",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",thumbnail="https://i.imgur.com/MW39IT7.jpg",folder=True)
    addDir(title="Now47",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",thumbnail="http://ecx.images-amazon.com/images/I/81ynokvm4ML._SL1500_.jpg",folder=True)
    addDir(title="Now46",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",thumbnail="https://i.imgur.com/k9rHGW4.jpg",folder=True)
    addDir(title="Now45",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",thumbnail="https://i.imgur.com/S3yz782.jpg",folder=True)
    addDir(title="Now44",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",thumbnail="https://i.imgur.com/3vIX3qz.jpg",folder=True)
    addDir(title="Now43",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_51+"/",thumbnail="https://i.imgur.com/BiuamOs.jpg",folder=True)
    addDir(title="Now42",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_52+"/",thumbnail="https://i.imgur.com/qG7Q3eB.jpg",folder=True)
    addDir(title="Now41",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_53+"/",thumbnail="https://i.imgur.com/fY12k8p.jpg",folder=True)
    addDir(title="Now40",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_54+"/",thumbnail="https://i.imgur.com/vqCADFb.jpg",folder=True)
    addDir(title="Now39",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",thumbnail="https://i.imgur.com/AlrMoZQ.jpg",folder=True)
    addDir(title="Now38",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-38-1024x1024.jpg",folder=True)
    addDir(title="Now37",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_57+"/",thumbnail="http://cps-static.rovicorp.com/3/JPG_400/MI0002/367/MI0002367718.jpg?partner=allrovi.com",folder=True)
    addDir(title="Now36",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_58+"/",thumbnail="https://i.imgur.com/sZJRcC9.jpg",folder=True)
    addDir(title="Now35",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_59+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-35-1024x1003.jpg",folder=True)
    addDir(title="Now34",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_60+"/",thumbnail="https://i.imgur.com/RX1UiHf.jpg",folder=True)
    addDir(title="Now33",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_61+"/",thumbnail="https://i.imgur.com/mBelz8G.jpg",folder=True)
    addDir(title="Now32",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_62+"/",thumbnail="https://i.imgur.com/6IjCOrH.jpg",folder=True)
    addDir(title="Now31",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_63+"/",thumbnail="https://i.imgur.com/ptKulfq.jpg",folder=True)
    addDir(title="Now30",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_64+"/",thumbnail="https://i.imgur.com/8ATx1WJ.jpg",folder=True)
    addDir(title="Now29",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_65+"/",thumbnail="https://i.imgur.com/jUJfKYw.jpg",folder=True)
    addDir(title="Now28",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_66+"/",thumbnail="https://i.imgur.com/SgvABNo.jpg",folder=True)
    addDir(title="Now27",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_67+"/",thumbnail="https://i.imgur.com/6kfTvcN.jpg",folder=True)
    addDir(title="Now26",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_68+"/",thumbnail="http://ecx.images-amazon.com/images/I/41cCLInJypL._SX355_.jpg",folder=True)
    addDir(title="Now25",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_69+"/",thumbnail="http://ecx.images-amazon.com/images/I/61TH%2BnVIC2L._SY300_.jpg",folder=True)
    addDir(title="Now24",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_70+"/",thumbnail="https://i.imgur.com/Cu6GDmE.jpg",folder=True)
    addDir(title="Now23",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_71+"/",thumbnail="https://i.imgur.com/wCnCP6p.jpg",folder=True)
    addDir(title="Now22",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_72+"/",thumbnail="http://www.music-bazaar.com/album-images/vol1/96/96327/612368-big/Now-That-S-What-I-Call-Music-22-cover.jpg",folder=True)
    addDir(title="Now21",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_73+"/",thumbnail="http://www.yosmusic.com/wp-content/uploads/2016/02/Now-21-%D7%97%D7%93%D7%A9.jpg",folder=True)
    addDir(title="Now20",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_74+"/",thumbnail="http://www.room512.co.uk/images/now20.jpg",folder=True)
    addDir(title="Now19",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_75+"/",thumbnail="http://ecx.images-amazon.com/images/I/61AMZA9HKDL.jpg",folder=True)
    addDir(title="Now18",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_76+"/",thumbnail="http://destinyxnowmusic.freehostia.com/nowmusic/nowisrael18.jpg",folder=True)
    addDir(title="Now17",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_77+"/",thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/1/14/Now17USA.jpg/220px-Now17USA.jpg",folder=True)
    addDir(title="Now16",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_78+"/",thumbnail="http://destinyxnowmusic.freehostia.com/nowmusic/nowisrael16.jpg",folder=True)
    addDir(title="Now15",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_79+"/",thumbnail="http://cps-static.rovicorp.com/3/JPG_400/MI0000/410/MI0000410973.jpg?partner=allrovi.com",folder=True)
    addDir(title="Now14",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_80+"/",thumbnail="http://destinyxnowmusic.freehostia.com/nowmusic/nowisrael14.jpg",folder=True)
    addDir(title="Now13",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_81+"/",thumbnail="https://agencyspace.files.wordpress.com/2013/01/13.jpg",folder=True)
    addDir(title="Now12",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_82+"/",thumbnail="https://i.imgur.com/drPUgJN.jpg",folder=True)
    addDir(title="Now11",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_83+"/",thumbnail="https://i.imgur.com/68McOMS.jpg",folder=True)
    addDir(title="Now10",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_84+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/61U1rUpKC2L.jpg",folder=True)
    addDir(title="Now9",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_85+"/",thumbnail="https://i.imgur.com/M1bTXsT.jpg",folder=True)
    addDir(title="Now8",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_86+"/",thumbnail="https://i.imgur.com/4a1Tq01.jpg",folder=True)
    addDir(title="Now7",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_87+"/",thumbnail="https://i.imgur.com/bYIICXG.jpg",folder=True)
    addDir(title="Now6",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_88+"/",thumbnail="http://ecx.images-amazon.com/images/I/818bzGDAdjL._SY355_.jpg",folder=True)
    addDir(title="Now5",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_89+"/",thumbnail="https://i.imgur.com/99gMxiW.jpg",folder=True)
    addDir(title="Now4",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_90+"/",thumbnail="https://upload.wikimedia.org/wikipedia/en/2/24/Now_4_US.jpg",folder=True)
    addDir(title="Now3",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_91+"/",thumbnail="https://i.imgur.com/Qg1ne42.jpg",folder=True)
    addDir(title="Now2",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_92+"/",thumbnail="https://i.imgur.com/P1S1mUZ.jpg",folder=True)
    addDir(title="Now1",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_93+"/",thumbnail="http://lifestoogood.net/wp-content/uploads/2011/10/Now-1-300x300.jpg",folder=True)
    addDir(title="NowChristmas",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_134+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/20150814114319/Christmas_Hi_Res-1024x901.jpg",folder=True)
    addDir(title="NowDriveTime",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_131+"/",thumbnail="https://i.imgur.com/ouTUu6F.jpg",folder=True)
    addDir(title="NowDanceHits",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_132+"/",thumbnail="https://i.imgur.com/3AbbPOW.jpg",folder=True)
    addDir(title="NowFitness",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_94+"/",thumbnail="https://i.imgur.com/L9ishX7.jpg",folder=True)
    addDir(title="NowBritHits",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_95+"/",thumbnail="https://i.imgur.com/xElLYIX.jpg",folder=True)
    addDir(title="NowPartyAnthems",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_96+"/",thumbnail="https://is3-ssl.mzstatic.com/image/thumb/Music6/v4/47/a4/ba/47a4ba2e-bd66-8663-b518-bf7364424b1b/05099931924153.jpg/1200x630bb.jpg",folder=True)
    addDir(title="NowClassicRock",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_97+"/",thumbnail="http://ecx.images-amazon.com/images/I/61IeOgC6FyL._SY300_.jpg",folder=True)
    addDir(title="NowPop",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_98+"/",thumbnail="http://dvfnvgxhycwzf.cloudfront.net/media/SharedImage/imageFull/.fgn3yf9U/SharedImage-54831.jpg?t=6f021b9c4b26aa96d828",folder=True)
    addDir(title="NowDisco",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_99+"/",thumbnail="http://724c8ec11924b4643ff4-cbc0e5c64c4e0e6a0ca4e8696c6ef08e.r74.cf3.rackcdn.com/5099940901527.jpg",folder=True)
    addDir(title="NowFeelGood",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_100+"/",thumbnail="https://i.imgur.com/tDOwhUf.jpg",folder=True)
    addDir(title="NowRunning",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_101+"/",thumbnail="http://tesco.scene7.com/is/image/tesco/521-8951_PI_1000025MN?id=6eebz3&fmt=jpg&fit=constrain,1&wid=250&hei=250",folder=True)
    addDir(title="NowSong",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_102+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/61wQSnctNeL.jpg",folder=True)
    addDir(title="NowSinger",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_103+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/61XfCx9YlWL.jpg",folder=True)
    addDir(title="NowHouse",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_104+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/81Tb8U3VvkL._SL1500_.jpg",folder=True)
    addDir(title="NowSummerParty",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_105+"/",thumbnail="http://direct-ns.rhap.com/imageserver/v2/albums/Alb.189415979/images/500x500.jpg",folder=True)
    addDir(title="NowSummer",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_106+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/81vNIT4a-6L._SL1500_.jpg",folder=True)
    addDir(title="NowDrive",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_107+"/",thumbnail="https://images-eu.ssl-images-amazon.com/images/I/61EoE0udUkL._SL500_AA280_.jpg",folder=True)
    addDir(title="NowMovies",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_108+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/81Faz2sWEnL._SX355_.jpg",folder=True)
    addDir(title="NowDisney",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_109+"/",thumbnail="http://ecx.images-amazon.com/images/I/819lN7C5loL._SL1500_.jpg",folder=True)
    addDir(title="NowReggae",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_110+"/",thumbnail="https://i.scdn.co/image/424aa797636f9477e07b1d168498c7c75c53a566",folder=True)
    addDir(title="NowRock",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_111+"/",thumbnail="http://loudwire.com/files/2016/01/unnamed-10.jpg",folder=True)
    addDir(title="NowCountry",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_112+"/",thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/8/88/Nowcountryfeat.jpg/220px-Nowcountryfeat.jpg",folder=True)
    addDir(title="NowLegends",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_113+"/",thumbnail="https://artwork-cdn.7static.com/static/img/sleeveart/00/039/687/0003968720_500.jpg",folder=True)
    addDir(title="NowPowerBallads",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_114+"/",thumbnail="https://i.imgur.com/NBeutUv.jpg",folder=True)
    addDir(title="Now80's",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_115+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/817iO3O9vfL._SL1500_.jpg",folder=True)
    addDir(title="Now90's",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_116+"/",thumbnail="http://tesco.scene7.com/is/image/tesco/493-2421_PI_1000025MN?wid=493&ht=538",folder=True)
    addDir(title="Now00's",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_117+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/now00s.jpg",folder=True)
    addDir(title="NowNo.1's",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_118+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOWno1s.jpg",folder=True)
    addDir(title="Now21stCentury",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_119+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/91wmfiSXm0L._SL1500_.jpg",folder=True)
    addDir(title="NowSing",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_135+"/",thumbnail="https://i.imgur.com/gws3kE1.jpg",folder=True)
    addDir(title="NowParty",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_136+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-Party-1024x1024.jpg",folder=True)
    addDir(title="NowRockBallads",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_137+"/",thumbnail="https://images-na.ssl-images-amazon.com/images/I/618hAw24%2BRL._SY300_.jpg",folder=True)
    addDir(title="NowChilled",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_120+"/",thumbnail="https://images-eu.ssl-images-amazon.com/images/I/61Q9IGKQZBL._SL500_AA280_.jpg",folder=True)
    addDir(title="NowMusicals",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_121+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOWMusicals2.png",folder=True)
    addDir(title="NowUSA",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_122+"/",thumbnail="http://ecx.images-amazon.com/images/I/81nq7JhBUUL._SL1417_.jpg",folder=True)
    addDir(title="Now25Years",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_123+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOW-25-Years.jpg",folder=True)
    addDir(title="Now30Years",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_124+"/",thumbnail="http://thelatest.co.uk/files/2013/05/Now-30-Years-Sleeve.jpg",folder=True)
    addDir(title="NowR&B",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_125+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/nowrb.jpeg",folder=True)
    addDir(title="NowMillion",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_126+"/",thumbnail="http://www.officialcharts.com/media/318845/now_thats_what_i_call_a_million.jpg?width=500&height=500",folder=True)
    addDir(title="NowClubHits",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_127+"/",thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOW-Club-Hits-1024x900.jpg",folder=True)
    addDir(title="NowLove",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_129+"/",thumbnail="https://upload.wikimedia.org/wikipedia/en/e/e2/Now_That's_What_I_Call_Love_3.jpg",folder=True)
    addDir(title="NowMusic",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_128+"/",thumbnail="http://a1491.phobos.apple.com/us/r30/Purple4/v4/c2/b7/97/c2b79704-18bf-960c-f5f6-877b12af4af1/mzl.vmknkzkm.png",folder=True)
    addDir(title="Now80sNew",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_148+"/",thumbnail="https://i.imgur.com/B1Nwd44.jpg",folder=True)
    xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)




