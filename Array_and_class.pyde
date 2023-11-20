class Planet:
    alien_count = 0
    name = " "
    
    #constructor
    def __init__(self, alien_count, name):
        self.alien_count = alien_count
        self.name = name
        
    def print_alien(self):
        print(alien_count)
        print(name)



def setup():
    size(500,500)
    colorMode(HSB)
    global planets, aliens
    
    mars = Planet(10, "mars")
    # global most
    # global least
    
    for planet in planets:
        print(planet)
        
    for alien in aliens:
        print(alien)
        
    # planets[0] = "bla"
        
    # print(planets[8])
        
    #planets[20] = "hello"
    
    #planets.reverse()
    
    # for i in range(len(planets) - 1, 0, -1):
    #     print(planets[i] + " " + str(aliens[i]))
    
    for i in range(len(planets)):
        print(planets[i] + " " + str(aliens[i]))
    
    # for current in aliens:
    #     if current > most:
    #         most = current
    # print("The most amount of aliens on a planet is", most)
    
    # for current in aliens:
    #     if current < least:
    #         least = current
    # print("The least amount of aliens on a planet is", least)
    
    # least_index = 0
    # for i in range(len(planets)):
    #     if aliens[i] < aliens[least_index]:
    #         least_index = i
            
    # print("Planet with the least number of aliens is : " + str(aliens[least_index]))
    
    most_index = 0
    for i in range(len(planets)):
        print(i)
        if aliens[i] > aliens[most_index]:
            most_index = i
            print("most_index: " + str(i))
            
    print("Planet with the most number of aliens is : " + str(aliens[most_index]))
    
    sum = 0
    for i in range(len(planets)):
        sum = sum + aliens[i]
        
    average = sum / len(planets)
    
    print("Total Aliens: " + str(sum))
    print("Average Aliens: " + str(average))
        
# most = 0
# least = 34
planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
aliens = [50, 130, 20, 100, 250, 340, 200, 200, 10]



def draw():
    global planets, aliens
    
    background(0)
    w = width / len(planets)
    print("w: " + str(w))
    # stroke(255)
    for i in range(len(planets)):
        x = w * i
        fill(i / float(len(planets)) * 255, 255, 255)
        rect(x, height, w, - aliens[i])
        textMode(CENTER, CENTER)
        fill(255)
        text(planets[i], x + (w * 0.5), height - 20)
        
        #should work
    
