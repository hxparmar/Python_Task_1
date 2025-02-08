#(Q) CREATE A SIMPLE TO-DO LIST APPLICATION USING FUNCTIONS. WAP PROGRAM THAT ALLOWS A USER TO MANAGE A SIMPLE TO-DO LIST. THE PROGRAM SHOULD OFFER THE FOLLOWING FUNCTIONALITY.abs

def to_do():
    d={}
    def task():
        i=0
        while i<4:
            print("************************************************\n")
            print("                TO-DO LIST                      \n")
            print("************************************************\n")

            disp=print("1.ADD A TASK\n2.REMOVE A TASK\n3.DISPLAY A TASK\n4.QUIT THE APP")
            inp=int(input("Give the number acording to the list of choice given:"))
            if inp==1:
                def add_task():
                    inp_task=int(input("\nEnter the number of task you want to add:"))
                    i=1
                    while i<=inp_task:
                        add=input("Enter task:")
                        d[i]=add
                        
                        i+=1
                    print("TASK ADDED TO THE LIST\n")
                add_task()
            elif inp==2:
                def remove_task():
                    if len(d)>0:
                        rem=int(input("Remove a task:"))
                        del d[rem]
                        print("\nTASK REMOVED\n")
                    elif len(d)==0:
                        print("\nNO TASK LEFT TO BE REMOVED\n")
                remove_task()
            elif inp==3:
                def disp_task():
                    i=0
                    t1=list(d.keys())
                    t2=list(d.values())
                    while i<len(t1):
                        if i<len(t1):
                            print("\nTASK.(",t1[i],") -->",t2[i],)
                        else:
                            print("\nNOTHING TO BE DISPLAYED\n")
                            break
                        i+=1
                disp_task()
            elif inp==4:
                print("\nEXITING THE APPLICATION\n")
                break
    task()
to_do()
        
                

                
    
