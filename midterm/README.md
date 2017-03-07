# Mid-term


midterm assignment for info 7374

Enron analysis:

	Firstly,I tried to figure out the "Yellow page" for the data set.After processing all the 		data, I get a basic key-value pair like 
	{useremail : {username: 	"xxxx",userFolderNumber"xxxx"}}.
	I chose usermail to be the key, because the name has too many different forms. Email 		address seems to be a better key.And the output is saved in an json file called 	    		"userinfo" with the ipynb.  
	
	Secondly, given the article related to the scandal, I intended to dig on the CEO 's email.
	Moreover, instead of scanning through his mail, I used his most frequent contactor in the 		data set, because I think normal employees might not watch thier mouth that carefully. And 		it's easy for you to locate such data set  since you got a yellow page.

	Finally , I scanned throughed DD's(the one the ceo talk to mostly) email and find the most 		often words that he uses.Not that much words related to the scandal as it appears. 


NYT analysis:

	Before start: I read through the NYT API and download all the articles in year 2015 and 	2016. I meaned to do the analysis first, narrowing the aspect I want tp dig into and go   		back to search for the particular subject. 

	Firstly,I tried to the figure out whether the press is controlled by a small group of 		writers. And did they hold a certain attitude to a topic? However, after I calculated all 		the numbers. Nothing was found and the most productive writer only contributed three 		articles to NYT a single year.
	
	Secondly,I tried to see for what subject do poeple concern about. I picked top ten words  		every month and "election" came in the first place and "books" came in second.I store all 		of those results in the "hotwords.json" with the ipynb.

	
	Finally, I search for the book in NYT database and try to figure out what did people talk 
	about the most. The results are stored in the" result.json".






