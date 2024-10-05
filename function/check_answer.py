"""for checking answer"""
def check_answer(ans,status,char):
    """check answer"""
    status = list(status)
    for i,_ in enumerate(status):
        #print(ans[i])
        if ans[i]==char and ans[i] not in status:
            status[i] = char
            break
    status = "".join(status)
    return status

check_answer("cyan","__an","c")