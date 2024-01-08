CREATE DATABASE IMG

USE IMG;

/*  Join / merge the files together into a single table. */

select * into data from
(select 
md.Date	
,rev.Day_Name
,rev.Week_ID
,rev.Month_ID
,DATEPART(week,md.Date) week_number
,rev.Month_Number
,rev.Year
,md.Promo
,vd.Visitors
,md.Marketing_spend
,rev.Revenue
from Marketing_Data md
left join Visitors_Data vd
on md.Date = vd.Date
left join 
(select * from revenue_data_1 
union all
select * from revenue_data_2) rev
on md.date = rev.date
) d


select * from data

/* delete from data where Revenue is null or Marketing_spend is null */


/* 	How much revenue did we generate in total and by campaign?*/

select promo,sum(revenue) as revenue from data
where revenue is not null and Marketing_Spend is not null
group by promo 

select sum(revenue) as [Total revenue] from data
where revenue is not null and Marketing_Spend is not null

/* 	Which day we had the highest average visitors? */

select date, Visitors from data
where Visitors = (select max(Visitors) from data)

/* 	Which promotion costs us the most? */
select top(1) promo,sum(Marketing_Spend) as Market_Spend from data
where revenue is not null and Marketing_Spend is not null
group by promo 
order by Market_Spend desc



/* 	What is the weekly average revenue, visitors and marketing spend? */
select AVG([weekly visitor]) [weekly Average visitor],round(AVG([weekly Marketing Spend]),1) [weekly Avearge Marketing Spend], AVG([weekly Revenue]) [weekly Average Revenue]
from (
select week_number week, Sum(visitors) [weekly visitor],Sum(marketing_spend) [weekly Marketing Spend], Sum(revenue) [weekly Revenue] from data
group by week_number
) innerquery


