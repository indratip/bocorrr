# -*- coding: utf-8 -*-
"""ngempeng.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g4R1VMxbvi17zecFOy2T_qM-0myMQzLZ
"""

! nvidia-smi -L

# Install colab_ssh
!pip install colab_ssh --upgrade

from colab_ssh import launch_ssh
launch_ssh('28xySP6UimwwTKLVQ8CPUE9uO2K_Xw8w2KCCuBStp92gCBXd92', '929239')
#@title **Colab Shutdown**

#@markdown To Kill NGROK Tunnel
NGROK = False #@param {type:'boolean'}

!sudo apt-get update && sudo apt-get upgrade

if Sleep:
    from time import sleep
    sleep(43200)