def update() :
    chai_type = "Elaichi"
    # if we not make this kicten inside the function - it will throw error
    def kicten() :
        # if we comment this nonlocal - it will not update chai_type value - because nonlocal is required
        # nonlocal chai_type 
        chai_type = "kesar"
    # this should be called outside the function 
    kicten();
    print("After kicten update", chai_type )

update()