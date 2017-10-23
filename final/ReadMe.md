# Final Exam - Analysis on 'Pokemon go' game data

## Main Idea:
This project mainly works on 4 data sets, two of which are downloaded and
two of which are acquired through APIs. The analysis focused on how to get
the most rare pokemon in the game 'Pokemon go' ,following through the steps :

1. pokemon ranking
2. factors that affect pokemon appearance
3. similarity between pokemon show-up patterns
4. capture rate
5. the pokemon 'nest' (where they show-up frequently)


### 1.analysis_1: pokemon ranking
####   0. data-set:
 'pokemon go csv', which contains all 150 pokemon individual datas. [data_set_link](https://www.kaggle.com/abcsds/pokemongo)
####  1. attempt:
1.find out the mean value(total value = CP + 0.8*HP) of each type
2.find out the best pokemon of each type
####  2. output:

| Type | Total pokemon number| value|
| ------| ------ | ------ |
| Bug |12 | 1298 |

| Type | Pokemon no. | name| value|
| ------| ------ | ------ | ------|
| Dragon | 149 | Dragonite |3649.8|

![Alt text](https://github.com/PandaKillsLot/7374-Data-analysis/blob/master/final/analysis/ana_1_output/ana_1_type_distribution.png)

![Alt text](https://github.com/PandaKillsLot/7374-Data-analysis/blob/master/final/analysis/ana_1_output/ana_1_poke_best.png)

#### &#160;3. conclusions:
CPs are pretty evenly distribution except that dragon type pokemons are so strong.

### 2. analysis_2: factors affect pokemon appearance
#### &#160;  0. data-set:
 '300k.csv',contains 300,000 pokeomon go appearance record  
 <font color=#00ffff size=20> I'm sorry that this dataset have to be download manually and put in path 'final/data/300k.csv'</font>

  [data_set_link](https://www.kaggle.com/semioniy/predictemall)
#### &#160;  1. attempt:
check the relation between 'pokemon appearance','day-time' and 'population_density', since 'day-time' and 'population_density'
are the two main elements announced in Nintendo's official statement which determines the appearance. 1.count the appearance rate. 2. count the appearance
rate in  three different times slot. 3.count the mean population of appearance.
#### &#160;  2. output:

| Pokemon no. | Name | Type |appearance rate| show_up_rate_in morning| show_up_rate_in evening| show_up_rate_in night| population_density|
| ------| ------ | ------ | ------|------ | ------|------ |---|
| 1 | Bulbasaur | Grass|0.121 |0.291401|0.253185|0.455414|1851.392773|


cp values and show-up rates:

![Alt text](https://github.com/PandaKillsLot/7374-Data-analysis/blob/master/final/analysis/ana_2_output/ana_2_cp_ap.png)

#### &#160;  3. conclusions:
The higher cp or hp, the more rarely the pokemon shows up. Nearly no pokemon showed up in the afternoon, maybe it's due to the data collection time.  Population_density does contribute to pokemons' appearance rate.
### 3. analysis_3: similarity between pokemon show-up patterns
#### &#160;  0. data-set:
 'df_poke_best_population_density.csv',output from ana_2 ;
'300k.csv',contains 300,000 pokeomon go appearance record [data_set_link](https://www.kaggle.com/semioniy/predictemall)
#### &#160;  1. attempt:
find pokemon patterns using k-means; 1.convert show up time into an one
-dimension array, and draw a scatter to see how many groups there are. 2. use k-means algorithm to define the cluster and assign each pokemon with an pattern group
#### &#160;  2. output:

| Pokemon no. | Name | Type |appearance rate| show_up_rate_in morning| show_up_rate_in evening| show_up_rate_in night| population_density|show_up_pattern|
| ------| ------ | ------ | ------|------ | ------|------ |---|----|
| 1 | Bulbasaur | Grass|0.121|0.291401|0.253185|0.455414|1851.392773|0|

before clustering

![Alt text](https://github.com/PandaKillsLot/7374-Data-analysis/blob/master/final/analysis/ana_3_output/ana_3_cluster_first.png)

clustering

![Alt text](https://github.com/PandaKillsLot/7374-Data-analysis/blob/master/final/analysis/ana_3_output/ana_3_cluster_after.png)

cluster cores

![Alt text](https://github.com/PandaKillsLot/7374-Data-analysis/blob/master/final/analysis/ana_3_output/ana_3_cluster_center.png)

#### &#160;  3. conclusions:
It's easy to see that time is not a problem but population matters. Pokemon didn't act in a certain pattern but when there is a lot of peolple, you will have a good hunt.


### 4. analysis_4: capture rate
#### &#160;  0. data-set:
'twitter_Snorlax_3.json' * 45,
using twitter api to search for '#pokemon_name'
#### &#160;  1. attempt:
I want to know that if a rare pokemon shows up, what's the capture rate? To get
the rate, I search tweets with specified tags and using nltk to do the analysis. The basic idea is that capture rate = capture times/ (capture times + flee times)
.So, firstly, to define what kind of tweet means a "capture", I tokenize and simplify the words to find the verb through verb-tags which means 'capture', like 'encounter'. And then, I  use wordnet to find all it's sys.
By checking the positive verb, I can count how many capture time that user tweeted. By the same way, I can get the flee time.
#### &#160;  2. output:

| Pokemon no. | Name | Type |appearance | population_density|capture_rate
| ------| ------ | ------ | ------|------ | ------|
| 149 | Dragonite | Dragon |0.291401|1851.392773|0.9|


![Alt text](https://github.com/PandaKillsLot/7374-Data-analysis/blob/master/final/analysis/ana_4_output/ana_4_capture_rate.png)

#### &#160;  3. conclusions:
The same as what I met up in the game, when a rare pokemon shows up, i always end up catching it. Though a rare pokemon may take you more balls and berries to capture it, they seldom flee. I guess Nintendo doesn't want to break players' heart since rare pokemon barely appears.



### 5. analysis_5: the pokemon 'nest' (where they show-up frequently)
#### &#160;  0. data-set:
 'GO_data_1.csv' ~ 'GO_data_30.csv', using google map api to convert the
coordinates into real world regions
#### &#160;  1. attempt:
I tried to figure out some hot spot so I can easily use fake gps apps to fly to those place to hunt pokemons.By using google api and nltk, I successfully points out the most hot pokemon spots in the US and find the location name in real world(county name and neighborhood name) by converting all coordinates into real world locations.
#### &#160;  2. output:
('Hidalgo County', 55), ('Tarrant County', 42), ('Denton County', 37), ('Galveston County', 27), ('Cameron County', 11), ('Fort Bend County', 8)
#### &#160;3. conclusions:
I thought NewYork city may win the game, however, it didn't come in the first place. So maybe there is some other elements worth digging. As Nintendo's official statement, a water type pokemon may appear more often near a river. Maybe parks or certain forests are as attractive as  population to pokemons. The good news is, at least I could use fake-gps apps to fly to Texas and enjoy a good time.
