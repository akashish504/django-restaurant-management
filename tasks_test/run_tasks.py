from mysite.tasks import update_status_accepted_to_preparing
import time

if __name__ == '__main__':
    # result = longtime_add.apply_async(args=[1,2], countdown = 10)
    
    result = update_status_accepted_to_preparing.apply_async(args=[1],countdown = 10)
    
    
    # at this time, our task is not finished, so it will return False
    # print ('Task finished? ', result.ready())
    # print ('Task result: ', result.result)
    # # sleep 10 seconds to ensure the task has been finished
    # # time.sleep(10)
    # # now the task should be finished and ready method will return True
    # print ('Task finished? ', result.ready())
    # print ('Task result: ', result.result)