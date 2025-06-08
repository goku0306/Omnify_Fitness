INSERT INTO ClassType (ClassTypeName, ClassTypeDesc, CreatedBy, CreatedOn, ClassTypeStatus)
VALUES 
('Yoga', 'Yoga for beginners', 1, GETDATE(), 1),
('Zumba', 'High energy Zumba class', 1, GETDATE(), 1);


INSERT INTO Instructor (InstructorName, InstructorDesc, ClassTypeID, CreatedBy, CreatedOn, InstructorStatus)
VALUES
('John Doe', 'Expert in Yoga', 1, 1, GETDATE(), 1),
('Jane Smith', 'Certified Zumba trainer', 2, 1, GETDATE(), 1);


INSERT INTO FitnessClass (FitnessClassName, ClassTypeID, InstructorID, ClassTime, TotalSlots,AvailbleSlots, CreatedBy, CreatedOn, FitnessClassStatus)
VALUES
('Morning Yoga', 1, 1, DATEADD(HOUR, 1, GETDATE()), 20,20, 1, GETDATE(), 1),
('Evening Zumba', 2, 2, DATEADD(HOUR, 5, GETDATE()), 30,30, 1, GETDATE(), 1);
