# datathon
# Government: Analyzing and Predicting Inbound Crossings the U.S.-Canada and the U.S.-Mexico border

The goal of our project this weekend was to analyze the effect of COVID-19 on inbound traffic crossings between the U.S.-Canada and the U.S.-Mexico border. We wanted to analyze the efficiency and volume of traffic at each entry port, looking for various factors affecting long wait times. Additionally, we wanted to provide a solution for our peers and fellow travelers to efficiently plan vacations across the border without dealing with unforeseen wait times. 

Initially to understand the data we conducted a descriptive analysis of our dataset after splitting it into two categories: Mexican borders and Canadian borders. This helped us narrow down each port and understand their traffic movements for their respective regions. Another factor we decided to include in our analysis is seasonal weather. We classified each month as a fall, spring, summer, or winter month. This showed us that during the summer and fall seasons, the Canadian border has the most inbound traffic while the Mexico border has constant high-volume traffic throughout every season. (Refer to visualization below 1.1). 

When comparing pre and post-Covid-19 inbound traffic volume, we noticed

### 2017-2019
<img width="593" alt="Screenshot 2024-05-19 at 11 06 39 AM" src="https://github.com/sbains2/datathon/assets/67097552/19542969-8c0d-4a15-b2ec-d526feddbedf">

### 2020-2021
<img width="399" alt="Screenshot 2024-05-19 at 11 07 13 AM" src="https://github.com/sbains2/datathon/assets/67097552/babc0663-9121-4fd2-8f2a-7d437b49f0dd">

### 2022-2024
<img width="599" alt="Screenshot 2024-05-19 at 11 08 01 AM" src="https://github.com/sbains2/datathon/assets/67097552/81f926db-76aa-4b0b-aed2-3a24b0028ac4">



<img width="567" alt="Screenshot 2024-05-19 at 10 58 07 AM" src="https://github.com/sbains2/datathon/assets/67097552/a21dfb10-400a-4c10-b267-193af51c6223">



After noticing such a discrepancy, we still were curious about the highly consistent trends of inbound traffic so we decided to further break down our two data of inbound traffic crossings between the U.S.-Canada and the U.S.-Mexico border into 3 new categories:
1. Distribution of inbound traffic for each port per year

   
           <Viz Canada 1.2.1> <Viz Mexico 1.2.2> 
3. Distribution of traffic per year at the Mexican border
          <Viz Canada 1.3.1> <Viz Mexico 1.3.2> 
4. Distribution of inbound traffic per state
          <Viz Canada 1.4.1> <Viz Mexico 1.4.2> 


   
## Data Metrics (Data Analysis)

To create an accurate measurement of the traffic at each port at the borders, we decided to norma<img width="1106" alt="Screenshot 2024-05-19 at 10 15 36 AM" src="https://github.com/sbains2/datathon/assets/67097552/e4d3ddd2-2df2-4204-b7e4-33cffbeab4f9">
lize the data points and compute an aggregated score, ranking each port based on the busiest port. To do so we created the following metric that encompassed the majority of the factors affecting border wait times.

Step 1: We normalized each measure on a scale of 0-1 by dividing by the maximum value of that value across all ports. 

          Normalized Measure = Max Measure Value/Measure Value

          # Normalize measures
          for the measure in measure_traffic_pivot.columns[1:]:
              measure_traffic_pivot[measure] = measure_traffic_pivot[measure] / measure_traffic_pivot[measure].max()

Step 2: We decided to assign a weight to each normalized measure. We assigned the weights based on the time taken to cross the border.

          weights = {
              'Bus Passengers': 0.1,	
              'Buses': 2,	
              'Pedestrians': 0.1,
              'Personal Vehicle Passengers': 0.1,
              'Personal Vehicles': 1,	
              'Rail Containers Empty': 0.2,
              'Rail Containers Loaded': 1,
              'Train Passengers': 0.1,
              'Trains': 2,
              'Truck Containers Empty': 0.2,
              'Truck Containers Loaded': 1,
              'Trucks': 2
          }
​
Step 3: After assigning weights to each variable and normalizing measures, we calculated the composite score by summing the weighted normalized measures.

          $$
          \sum_{i=1}^{n} w_{i} \times \text{Normalized Measure}_{i}
          $$
          
          measure_traffic_pivot['Composite Metric'] = sum(
              weights[measure] * measure_traffic_pivot[measure] for measure in weights
          )
​
Step 4: Now that the composite metric has been created, all we had to do was rank the ports

          port_metrics['Rank'] = port_metrics['Composite Metric'].rank(ascending=False)
          port_metrics = port_metrics.sort_values('Rank')


### Outcome:
This metric not only helped us understand the busiest ports during a certain time of the year but also helped us create a machine-learning model recommendation system, providing individuals entering the US with optimized information regarding which is the best port to use based on the date of travel. Our algorithm created above to compute the composite metric showed to have an 85% feature importance on predicting recommended ports for users.

<img width="886" alt="Screenshot 2024-05-19 at 9 36 11 AM" src="https://github.com/sbains2/datathon/assets/67097552/c79f0cea-5189-4d49-adc6-a1ef7bbafde2">

With the new composite metric having such an effect on the prediction values, we decided to rank each port from most busiest to least, using composite metric. We were able to implement this ranking system on our map visualization showing the top 20 locations that are the busiest that are recommended to avoid. While this may not seem like much, from this composite score we can infer:
- Ports with higher ranks might need to allocate more resources, infrastructure, and staffing to handle high traffic.
- By identifying the busiest ports, officials can optimize operations at these locations.
- Ports with the busiest wait time can strategically plan for future investments and expansion projects.
- The ranks highlight whether traffic is concentrated in a few major ports or more evenly distributed across several ports, helping guide policies to balance traffic loads and avoid bottlenecks.
- Critical ports that need robust emergency and contingency planning.

  Link to map: https://public.tableau.com/app/profile/sahil.bains/viz/MeasuringDensityAmongTop20RankedBusiestBorderCrossings/Sheet2
  


