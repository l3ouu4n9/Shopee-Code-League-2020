# Logistics Performance

Due to the recent COVID-19 pandemic across the globe, many individuals are increasingly turning to online platforms like Shopee to purchase their daily necessities. This surge in online orders has placed a strain onto Shopee and our logistics providers but customer expectations on the timely delivery of their goods remain high. On-time delivery is arguably one of the most important factors of success in the eCommerce industry and now more than ever, we need to ensure the orders reach our buyers on time in order to build our users’ confidence in us.

In order to handle the millions of parcels that need to be delivered everyday, we have engaged multiple logistics providers across the region. Only the best logistics providers that are able to meet Shopee’s delivery standards are partnered with us.

The performance of these providers is monitored regularly and each provider is held accountable based on the Service Level Agreements (SLA). Late deliveries are flagged out and penalties are imposed on the providers to ensure they perform their utmost.

The consistent monitoring and process of holding our logistics providers accountable allows us to maintain our promise of timely deliveries to our buyers.

# Task

Identify all the orders that are considered late depending on the Service Level Agreements (SLA) with our Logistics Provider.

For the purpose of this question, assume that all deliveries are considered successful by the second attempt.

# Basic Concepts

- Each orderid represents a distinct transaction on Shopee.
- SLA can vary across each route (A route is defined as Seller’s Location to Buyer’s Location) - Refer to SLA_matrix.xlsx
- Pick Up Time is defined as the time when the 3PL picks up the parcel and begins to process for delivery. It marks the start of the SLA calculation.
- Delivery Attempt is defined as an attempt made by the 3PL to deliver the parcel to the customer. It may or may not be delivered successfully. In the case when it is unsuccessful, a 2nd attempt will be made. A parcel that has no 2nd attempt is deemed to have been successfully delivered on the 1st attempt.
- All time formats are stored in epoch time based on Local Time (GMT+8).
- Only consider the date when determining if the order is late; ignore the time.
- Working Days are defined as Mon - Sat, Excluding Public Holidays.
- SLA calculation begins from the next day after pickup (Day 0 = Day of Pickup; Day 1 = Next Day after Pickup)

2nd Attempt must be no later than 3 working days after the 1st Attempt, regardless of origin to destination route (Day 0 = Day of 1st Attempt; Day 1 = Next Day after 1st Attempt).
Only consider the date when determining if the order is late; ignore the time.

Assume the following Public Holidays: 
1. 2020-03-08 (Sunday);
2. 2020-03-25 (Wednesday);
3. 2020-03-30 (Monday);
4. 2020-03-31 (Tuesday)

# Submission Format

Check each delivery order and determine whether it is late.
Two columns required:
- orderid.
- is_late: assign value 1 if the order is late, otherwise 0.

# Final Score
0.47625