import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

QUESTION_PATH=os.path.join(BASE_DIR,'db','subject')
CUSTOMER_PATH=os.path.join(BASE_DIR,'db','customer')
RECORD_PATH=os.path.join(BASE_DIR,'db','record')
PRIZE_PATH=os.path.join(BASE_DIR,'db','prize')
C2P_PATH=os.path.join(BASE_DIR,'db','customer_to_prize')
