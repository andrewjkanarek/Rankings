from league import *

# def updatePR(vertex, v_scores):
# 	x = (1 - damp) / len(vertices)
# 	curr_sum = 0
# 	# print "current vertex: " + vertex
# 	for v in vertices[vertex][1]:
# 		# print v + ": " + str(vertex_scores[v]) + " " + str(len(vertices[v][0]))
# 		curr_sum += (vertex_scores[v] / len(vertices[v][0]))

# 	curr_sum *= damp
# 	v_scores[vertex] = curr_sum + x

league = League()

#Teams
#Michigan -
#Ohio -
#Wisconsin -
#Purdue -
#Rutgers -
#Illinois -

#Indiana -
#Northwestern -
#Iowa -
#Maryland

# Michigan games
league.addGame("Michigan", "Wisconsin")
league.addGame("Michigan", "Rutgers")
league.addGame("Michigan", "Illinois")
league.addGame("Michigan", "Ohio")
league.addGame("Purdue", "Michigan")
league.addGame("Michigan", "Indiana")
league.addGame("Michigan", "Iowa")
league.addGame("Michigan", "Northwestern")
league.addGame("Maryland", "Michigan")

# Purdue games
league.addGame("Purdue", "Rutgers")
league.addGame("Purdue", "Indiana")
league.addGame("Purdue", "Wisconsin")
league.addGame("Purdue", "Illinois")
league.addGame("Purdue", "Maryland")
league.addGame("Iowa", "Purdue")
league.addGame("Northwestern", "Purdue")
league.addGame("Ohio", "Purdue")

#Wisconsin games
league.addGame("Wisconsin", "Illinois")
league.addGame("Wisconsin", "Rutgers")
league.addGame("Wisconsin", "Ohio")
league.addGame("Indiana", "Wisconsin")
league.addGame("Wisconsin", "Northwestern")
league.addGame("Wisconsin", "Iowa")
league.addGame("Maryland", "Wisconsin")

#Illinois games
league.addGame("Illinois", "Rutgers")
league.addGame("Illinois", "Ohio")
league.addGame("Indiana", "Illinois")
league.addGame("Northwestern", "Illinois")
league.addGame("Illinois", "Iowa")
league.addGame("Maryland", "Illinois")

#Ohio Games
league.addGame("Ohio", "Rutgers")
league.addGame("Indiana", "Ohio")
league.addGame("Northwestern", "Ohio")
league.addGame("Iowa", "Ohio")
league.addGame("Maryland", "Ohio")

#Rutgers games
league.addGame("Indiana", "Rutgers")
league.addGame("Northwestern", "Rutgers")
league.addGame("Iowa", "Rutgers")
league.addGame("Maryland", "Rutgers")


#Maryland Games
league.addGame("Maryland", "Indiana")
league.addGame("Maryland", "Northwestern")
league.addGame("Maryland", "Iowa")

#Indiana Games
league.addGame("Indiana", "Northwestern")
league.addGame("Indiana", "Iowa")

#Iowa Games
league.addGame("Iowa", "Northwestern")

#Northwestern Games




# 3 GAMES





print "Num Teams: " + str(league.getNumTeams())
print "Num Games: " + str(league.getNumGames())


print "TEAMS"
league.printTeams()

league.printRecords()

league.initializeScores();

league.printScores();



# temp_scores = dict(vertex_scores)
# 		for vertex in vertices:
# 			updatePR(vertex, temp_scores)
# 		convergence = checkConvergence(vertex_scores, temp_scores, thresh)
# 		vertex_scores = dict(temp_scores)
# 		num_iterations += 1


league.updateScores()
league.printScores()

league.updateScores()
league.printScores()

league.updateScores()
league.printScores()

league.updateScores()
league.printScores()

league.updateScores()
league.printScores()

league.updateScores()
league.printScores()

league.updateScores()
league.printScores()

league.updateScores()
league.printScores()




print ""
print ""
print ""
print ""

league2 = League()



league2.addGame("Michigan", "Purdue")
league2.addGame("Michigan", "Ohio")
league2.addGame("Michigan", "Maryland")

league2.addGame("Maryland", "Purdue")
league2.addGame("Maryland", "Ohio")

league2.addGame("Purdue", "Ohio")

print "Num Teams: " + str(league2.getNumTeams())
print "Num Games: " + str(league2.getNumGames())
league2.printRecords()

league2.initializeScores();

league2.printScores();

league2.updateScores()
league2.printScores()

league2.updateScores()
league2.printScores()








