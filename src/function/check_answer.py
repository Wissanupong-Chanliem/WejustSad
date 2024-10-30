"""for checking answer"""
def check_answer(ans:str,status:str,char:str):
    """check answer"""
    status = list(status)
    for i,_ in enumerate(status):
        #print(ans[i])
        if ans[i].lower() == char.lower() or not ans[i].isalpha():
            status[i] = ans[i]
            #break
    status = "".join(status)
    return status
