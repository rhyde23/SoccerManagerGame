#Schedule
import random
from stadiums import get_stadium
from months_in_order import get_number_month

schedule_prem = """
Saturday 12 September
12:30 Fulham v Arsenal (BT Sport)
15:00 Crystal Palace v Southampton (BT Sport)
17:30 Liverpool v Leeds (Sky Sports)
20:00 West Ham v Newcastle (Sky Sports)

Sunday 13 September
14:00 West Brom v Leicester (Sky Sports)
16:30 Spurs v Everton (Sky Sports)

Monday 14 September
18:00 Sheffield Utd v Wolves (Sky Sports)
20:15 Brighton v Chelsea (Sky Sports)

Saturday 19 September
12:30 Everton v West Brom (BT Sport)
15:00 Leeds v Fulham (BT Sport)
17:30 Man Utd v Crystal Palace (Sky Sports)
20:00 Arsenal v West Ham (Sky Sports)

Sunday 20 September
12:00 Southampton v Spurs (BT Sport)
14:00 Newcastle v Brighton (Sky Sports)
16:30 Chelsea v Liverpool (Sky Sports)
19:00 Leicester v Burnley (BBC Sport)

Monday 21 September
18:00 Aston Villa v Sheffield Utd (Sky Sports)
20:15 Wolves v Man City (Sky Sports)

Saturday 26 September
12:30 Brighton v Man Utd (BT Sport)
15:00 Crystal Palace v Everton (Amazon Prime)
17:30 West Brom v Chelsea (Sky Sports)
20:00 Burnley v Southampton (Sky Sports)

Sunday 27 September
12:00 Sheffield Utd v Leeds (BT Sport)
14:00 Spurs v Newcastle (Sky Sports)
16:30 Man City v Leicester (Sky Sports)
19:00 West Ham v Wolves (BT Sport)

Monday 28 September
17:45 Fulham v Aston Villa (Sky Sports)
20:00 Liverpool v Arsenal (Sky Sports) 

Saturday 3 October
12:30 Chelsea v Crystal Palace (BT Sport)
15:00 Everton v Brighton (BT Sport)
17:30 Leeds v Man City (Sky Sports)
20:00 Newcastle v Burnley (Sky Sports)

Sunday 4 October 
12:00 Leicester v West Ham (BT Sport)
12:00 Southampton v West Brom (BT Sport)
14:00 Arsenal v Sheffield Utd (Sky Sports)
14:00 Wolves v Fulham (Sky Sports)
16:30 Man Utd v Spurs (Sky Sports)
19:15 Aston Villa v Liverpool (Sky Sports)

Saturday 17 October
12:30 Everton v Liverpool (BT Sport)
15:00 Chelsea v Southampton (BT Sport Box Office)
17:30 Man City v Arsenal (Sky Sports)
20:00 Newcastle v Man Utd (Sky Sports Box Office)

Sunday 18 October
12:00 Sheffield Utd v Fulham (BT Sport Box Office)
14:00 Crystal Palace v Brighton (Sky Sports)
16:30 Spurs v West Ham (Sky Sports)
19:15 Leicester v Aston Villa (Sky Sports Box Office)

Monday 19 October
17:30 West Brom v Burnley (Sky Sports Box Office)
20:00 Leeds v Wolves (Sky Sports)

Friday 23 October
20:00 Aston Villa v Leeds

Saturday 24 October
12:30 West Ham v Man City (BT Sport)
15:00 Fulham v Crystal Palace (BT Sport Box Office)
17:30 Man Utd v Chelsea (Sky Sports)
20:00 Liverpool v Sheffield Utd (Sky Sports Box Office)

Sunday 25 October
14:00 Southampton v Everton (Sky Sports)
16:30 Wolves v Newcastle (Sky Sports)
19:15 Arsenal v Leicester (Sky Sports Box Office)

Monday 26 October
17:30 Brighton v West Brom (Sky Sports Box Office)
20:00 Burnley v Spurs (Sky Sports)

Friday 30 October
20:00 Wolves v Crystal Palace (BT Sport Box Office)

Saturday 31 October
12:30 Sheffield Utd v Man City (BT Sport)
15:00 Burnley v Chelsea (BT Sport Box Office)
17:30 Liverpool v West Ham (Sky Sports)

Sunday 1 November
12:00 Aston Villa v Southampton (Sky Sports Box Office)
14:00 Newcastle v Everton (Sky Sports)
16:30 Man Utd v Arsenal (Sky Sports)
19:15 Spurs v Brighton (Sky Sports Box Office)

Monday 2 November
17:30 Fulham v West Brom (Sky Sports Box Office)
20:00 Leeds v Leicester (Sky Sports)

Friday 6 November
17:30 Brighton v Burnley (Sky Sports Box Office)
20:00 Southampton v Newcastle (Sky Sports)

Saturday 7 November
12:30 Everton v Man Utd (BT Sport)
15:00 Crystal Palace v Leeds (BT Sport Box Office)
17:30 Chelsea v Sheffield Utd (Sky Sports)
20:00 West Ham v Fulham (BT Sport Box Office)

Sunday 8 November
12:00 West Brom v Spurs (Sky Sports Box Office)
14:00 Leicester v Wolves (Sky Sports)
16:30 Man City v Liverpool (Sky Sports)
19:15 Arsenal v Aston Villa (Sky Sports Box Office)

Saturday 21 November
12:30 Newcastle v Chelsea (BT Sport)
15:00 Aston Villa v Brighton (BT Sport)
17:30 Spurs v Man City (Sky Sports)
20:00 Man Utd v West Brom (BT Sport) 

Sunday 22 November
12:00 Fulham v Everton (BBC Sport)
14:00 Sheffield Utd v West Ham (Sky Sports)
16:30 Leeds v Arsenal (Sky Sports)
19:15 Liverpool v Leicester (Sky Sports)

Monday 23 November
17:30 Burnley v Crystal Palace (Sky Sports)
20:00 Wolves v Southampton (Sky Sports)

Friday 27 November
20:00 Crystal Palace v Newcastle (Amazon Prime Video)

Saturday 28 November
12:30 Brighton v Liverpool (BT Sport)
15:00 Man City v Burnley (BT Sport)
17:30 Everton v Leeds (Sky Sports)
20:00 West Brom v Sheffield Utd (Sky Sports)

Sunday 29 November
14:00 Southampton v Man Utd (Sky Sports)
16:30 Chelsea v Spurs (Sky Sports)
19:15 Arsenal v Wolves (Sky Sports)

Monday 30 November
17:30 Leicester v Fulham (Sky Sports)
20:00 West Ham v Aston Villa (Sky Sports)

Friday 4 December
20:00 Aston Villa v Newcastle (Sky Sports)

Saturday 5 December
12:30 Burnley v Everton (BT Sport)
15:00 Man City v Fulham (BT Sport)
17:30 West Ham v Man Utd (Sky Sports)
20:00 Chelsea v Leeds (Sky Sports)

Sunday 6 December
12:00 West Brom v Crystal Palace (Sky Sports)
14:15 Sheffield Utd v Leicester (Sky Sports)
16:30 Spurs v Arsenal (Sky Sports)
19:15 Liverpool v Wolves (Amazon Prime Video)

Monday 7 December
20:00 Brighton v Southampton (Sky Sports)

Friday 11 December
20:00 Leeds v West Ham (Sky Sports)

Saturday 12 December
12:30 Wolves v Aston Villa (BT Sport)
15:00 Newcastle v West Brom (Sky Sports)
17:30 Man Utd v Man City (Sky Sports)
20:00 Everton v Chelsea (BT Sport) 

Sunday 13 December
12:00 Southampton v Sheff Utd (Sky Sports)
14:15 Crystal Palace v Spurs (Sky Sports)
16:30 Fulham v Liverpool (Sky Sports)
19:15 Arsenal v Burnley (Sky Sports)
19:15 Leicester v Brighton (Amazon Prime Video)

Tuesday 15 December
18:00 Wolves v Chelsea (Amazon Prime Video)
20:00 Man City v West Brom (Amazon Prime Video)

Wednesday 16 December
18:00 Arsenal v Southampton (Amazon Prime Video)
18:00 Leeds v Newcastle (Amazon Prime Video)
18:00 Leicester v Everton (Amazon Prime Video)
20:00 Fulham v Brighton (Amazon Prime Video)
20:00 Liverpool v Spurs (Amazon Prime Video)
20:00 West Ham v Crystal Palace (Amazon Prime Video)

Thursday 17 December
18:00 Aston Villa v Burnley (Amazon Prime Video)
20:00 Sheffield Utd v Man Utd (Amazon Prime Video)

Saturday 19 December
12:30 Crystal Palace v Liverpool (BT Sport)
15:00 Southampton v Man City (Amazon Prime Video)
17:30 Everton v Arsenal (Sky Sports)
20:00 Newcastle v Fulham (Sky Sports)

Sunday 20 December
12:00 Brighton v Sheffield Utd (Sky Sports)
14:15 Spurs v Leicester (Sky Sports)
16:30 Man Utd v Leeds (Sky Sports)
19:15 West Brom v Aston Villa (BT Sport)

Monday 21 December
17:30 Burnley v Wolves (Sky Sports)
20:00 Chelsea v West Ham (Sky Sports)

Saturday 26 December
12:30 Leicester v Man Utd (BT Sport)
15:00 Aston Villa v Crystal Palace (BBC)
15:00 Fulham v Southampton (Sky Sports)
17:30 Arsenal v Chelsea (Sky Sports)
20:00 Man City v Newcastle (BT Sport)
20:00 Sheffield Utd v Everton (BT Sport)

Sunday 27 December
12:00 Leeds v Burnley (Sky Sports)
14:15 West Ham v Brighton (Sky Sports)
16:30 Liverpool v West Brom (Sky Sports)
19:15 Wolves v Spurs (Sky Sports)

Monday 28 December
15:00 Crystal Palace v Leicester (Amazon Prime Video)
17:30 Chelsea v Aston Villa (Amazon Prime Video)
20:00 Everton v Man City (Amazon Prime Video)

Tuesday 29 December
18:00 Brighton v Arsenal (Amazon Prime Video)
18:00 Burnley v Sheffield Utd (Amazon Prime Video)
18:00 Southampton v West Ham (Amazon Prime Video)
18:00 West Brom v Leeds (Amazon Prime Video)
20:00 Man Utd v Wolves (Amazon Prime Video)

Wednesday 30 December
18:00 Spurs v Fulham (Amazon Prime Video)
20:00 Newcastle v Liverpool (Amazon Prime Video)

Friday 1 January
17:30 Everton v West Ham (BT Sport)
20:00 Man Utd v Aston Villa (Sky Sports)

Saturday 2 January
12:30 Spurs v Leeds (BT Sport)
15:00 Crystal Palace v Sheff Utd (Sky Sports)
17:30 Brighton v Wolves (Sky Sports)
20:00 West Brom v Arsenal (BT Sport)

Sunday 3 January
12:00 Burnley v Fulham (Sky Sports)
14:15 Newcastle v Leicester (Sky Sports)
16:30 Chelsea v Man City (Sky Sports)

Monday 4 January
20:00 Southampton v Liverpool (Sky Sports)

*Matchweek 18 fixtures have been split between 12-14 January and 19-21 January and are signified by an asterisk.

Tuesday 12 January
18:00 Sheff Utd v Newcastle (Sky Sports)*
20:15 Wolves v Everton (Sky Sports)*
20:15 Burnley v Man Utd (Sky Sports)

Wednesday 13 January
18:00 Man City v Brighton (BT Sport)*
20:15 Aston Villa v Spurs (Sky Sports)*

Thursday 14 January
20:00 Arsenal v Crystal Palace (Sky Sports)*

Friday 15 January
20:00 Fulham v Chelsea (Sky Sports)

Saturday 16 January
12:30 Wolves v West Brom (BT Sport)
15:00 Leeds v Brighton (Sky Sports)
15:00 West Ham v Burnley (Amazon Prime)
17:30 Aston Villa v Everton (Sky Sports)
20:00 Leicester v Southampton (BT Sport)

Sunday 17 January
14:00 Sheffield Utd v Spurs (Sky Sports)
16:30 Liverpool v Man Utd (Sky Sports)
19:15 Man City v Crystal Palace (Sky Sports)

Monday 18 January
20:00 Arsenal v Newcastle (Sky Sports)

Tuesday 19 January
18:00 West Ham v West Brom (BT Sport)*
20:15 Leicester v Chelsea (Sky Sports)*

Wednesday 20 January
18:00 Man City v Aston Villa (BT Sport)
20:15 Fulham v Man Utd (BT Sport)*

Thursday 21 January
20:00 Liverpool v Burnley (Sky Sports)*

Saturday 23 January
20:00 Aston Villa v Newcastle (Sky Sports)

Tuesday 26 January
18:00 Crystal Palace v West Ham (BT Sport)
18:00 Newcastle v Leeds (BT Sport)
20:15 Southampton v Arsenal (BT Sport)
20:15 West Brom v Man City (BT Sport)

Wednesday 27 January
18:00 Burnley v Aston Villa (BT Sport)
18:00 Chelsea v Wolves (BT Sport)
19:30 Brighton v Fulham (BT Sport) 
20:15 Everton v Leicester (BT Sport)
20:15 Man Utd v Sheffield Utd (BT Sport)

Thursday 28 January
20:00 Spurs v Liverpool (BT Sport)

Saturday 30 January
12:30 Everton v Newcastle (BT Sport)
15:00 Crystal Palace v Wolves (Sky Sports)
15:00 Man City v Sheffield Utd (Sky Sports)
15:00 West Brom v Fulham (BT Sports)
17:30 Arsenal v Man Utd (Sky Sports)
20:00 Southampton v Aston Villa (Sky Sports)

Sunday 31 January
12:00 Chelsea v Burnley (BT Sport)
14:00 Leicester v Leeds (Sky Sports)
16:30 West Ham v Liverpool (Sky Sports)
19:15 Brighton v Spurs (Sky Sports)

Tuesday 2 February 
18:00 Sheffield Utd v West Brom (BT Sport)
18:00 Wolves v Arsenal (BT Sport)
20:15 Man Utd v Southampton (BT Sport)
20:15 Newcastle v Crystal Palace (BT Sport)

Wednesday 3 February
18:00 Burnley v Man City (BT Sport)
18:00 Fulham v Leicester (BT Sport)
19:30 Leeds v Everton (BT Sport)
20:15 Aston Villa v West Ham (BT Sport)
20:15 Liverpool v Brighton (BT Sport)

Thursday 4 February
20:00 Spurs v Chelsea (BT Sport)

Saturday 6 February
12:30 Aston Villa v Arsenal (BT Sport)
15:00 Burnley v Brighton (Sky Sports)
15:00 Newcastle v Southampton (BT Sport)
17:30 Fulham v West Ham (Sky Sports)
20:00 Man Utd v Everton (Sky Sports)*
(*moved from 8 Feb for FA Cup match) 

Sunday 7 February
12:00 Spurs v West Brom (BT Sport)
14:00 Wolves v Leicester (Sky Sports)
16:30 Liverpool v Man City (Sky Sports)
19:15 Sheffield Utd v Chelsea (Sky Sports)

Monday 8 February 
20:00 Leeds v Crystal Palace (Sky Sports)

Saturday 13 February
12:30 Leicester v Liverpool (BT Sport)
15:00 Crystal Palace v Burnley (Sky Sports)
17:30 Man City v Spurs (Sky Sports)
20:00 Brighton v Aston Villa (Sky Sports)

Sunday 14 February 
12:00 Southampton v Wolves (Amazon Prime)
14:00 West Brom v Man Utd (Sky Sports)
16:30 Arsenal v Leeds (Sky Sports)
19:00 Everton v Fulham (BT Sport)

Monday 15 February 
18:00 West Ham v Sheffield Utd (BT Sport)
20:00 Chelsea v Newcastle (Sky Sports)

Wednesday 17 February 
18:00 Burnley v Fulham (Sky Sports)
20:15 Everton v Man City (Amazon Prime)

Friday 19 February 
20:00 Wolves v Leeds (BT Sport)

Saturday 20 February
12:30 Southampton v Chelsea (BT Sport)
15:00 Burnley v West Brom (Sky Sports)
17:30 Liverpool v Everton (Sky Sports)
20:00 Fulham v Sheffield Utd (Sky Sports)

Sunday 21 February 
12:00 West Ham v Spurs (Sky Sports)
14:00 Aston Villa v Leicester (Sky Sports)
16:30 Arsenal v Man City (Sky Sports)
19:00 Man Utd v Newcastle (BT Sport)

Monday 22 February 
20:00 Brighton v Crystal Palace (Sky Sports)

Tuesday 22 February 
18:00 Leeds v Southampton (Sky Sports)

Saturday 27 February
12:30 Man City v West Ham (BT Sport)
15:00 West Brom v Brighton (Sky Sports)
17:30 Leeds v Aston Villa (Sky Sports)
20:00 Newcastle v Wolves (Sky Sports)

Sunday 28 February
12:00 Crystal Palace v Fulham (BBC)
12:00 Leicester v Arsenal (BT Sport)
14:00 Spurs v Burnley (Sky Sports)
16:30 Chelsea v Man Utd (Sky Sports)
19:15 Sheffield Utd v Liverpool (Sky Sports)

Monday 1 March 
20:00 Everton v Southampton (Sky Sports)

Tuesday 2 March
20:00 Man City v Wolves (BT Sport)

Wednesday 3 March
18:00 Burnley v Leicester (Sky Sports)
18:00 Sheff Utd v Aston Villa (BT Sport)
20:15 Crystal Palace v Man Utd (Sky Sports)

Thursday 4 March
18:00 Fulham v Spurs (BT Sport)
18:00 West Brom v Everton (Sky Sports)
20:15 Liverpool v Chelsea (Sky Sports)

Saturday 6 March
12:30 Burnley v Arsenal (BT Sport)
15:00 Sheff Utd v Southampton (Sky Sports)
17:30 Aston Villa v Wolves (Sky Sports)
20:00 Brighton v Leicester (Sky Sports)

Sunday 7 March
12:00 West Brom v Newcastle (Amazon Prime)
14:00 Liverpool v Fulham (Sky Sports)
16:30 Man City v Man Utd (Sky Sports)
19:15 Spurs v Crystal Palace (Sky Sports)

Monday 8 March
18:00 Chelsea v Everton (BT Sport)
20:00 West Ham v Leeds (Sky Sports)

Wednesday 10 March
18:00 Man City v Southampton (Sky Sports)

Friday 12 March
20:00 Newcastle v Aston Villa (BT Sport)

Saturday 13 March
12:30 Leeds v Chelsea (BT Sport)
15:00 Crystal Palace v West Brom (Sky Sports)
17:30 Everton v Burnley (Sky Sports)
20:00 Fulham v Man City (BT Sport)

Sunday 14 March
12:00 Southampton v Brighton (BBC)
14:00 Leicester v Sheffield United (Sky Sports)
16:30 Arsenal v Spurs (Sky Sports)
19:15 Man Utd v West Ham (Sky Sports)

Monday 15 March
20:00 Wolves v Liverpool (Sky Sports)

Friday 19 March
20:00 Fulham v Leeds (Sky Sports)

Saturday 20 March
20:00 Brighton v Newcastle (Sky Sports)

Sunday 21 March
15:00 West Ham v Arsenal (Sky Sports)
19:30 Aston Villa v Spurs (Sky Sports)

(all times BST)

Saturday 3 April
12:30 Chelsea v West Brom (BT Sport)
15:00 Leeds v Sheff Utd (Amazon Prime)
17:30 Leicester v Man City (Sky Sports)
20:00 Arsenal v Liverpool (Sky Sports)

Sunday 4 April
12:00 Southampton v Burnley (Sky Sports)
14:05 Newcastle v Spurs (Sky Sports)
16:30 Aston Villa v Fulham (Sky Sports) 
19:30 Man Utd v Brighton (BT Sport)

Monday 5 April
18:00 Everton v Crystal Palace (Sky Sports)
20:15 Wolves v West Ham (Sky Sports)

Friday 9 April
20:00 Fulham v Wolves (BT Sport)

Saturday 10 April
12:30 Man City v Leeds (BT Sport)
15:00 Liverpool v Aston Villa (Sky Sports)
17:30 Crystal Palace v Chelsea (Sky Sports)

Sunday 11 April
12:00 Burnley v Newcastle (Sky Sports)
14:05 West Ham v Leicester (Sky Sports)
16:30 Spurs v Man Utd (Sky Sports)
19:00 Sheff Utd v Arsenal (BT Sport)

Monday 12 April
18:00 West Brom v Southampton (Sky Sports)
20:15 Brighton v Everton (Sky Sports)

Friday 16 April
20:00 Everton v Spurs (Sky Sports)

Saturday 17 April
12:30 Newcastle v West Ham (Sky Sports)
20:15 Wolves v Sheff Utd (Sky Sports)

Sunday 18 April
13:30 Arsenal v Fulham (Sky Sports)
16:00 Man Utd v Burnley (Sky Sports)

Monday 19 April
20:00 Leeds v Liverpool (Sky Sports)

Tuesday 20 April
20:00 Chelsea v Brighton (Sky Sports)

Wednesday 21 April
18:00 Spurs v Southampton (Sky Sports)
20:15 Aston Villa v Man City (Sky Sports)

Thursday 22 April
20:00 Leicester v West Brom (BT Sport)

Friday 23 April
20:00 Arsenal v Everton (Sky Sports)

Saturday 24 April
12:30 Liverpool v Newcastle (BT Sport)
17:30 West Ham v Chelsea (Sky Sports)
20:00 Sheff Utd v Brighton (Sky Sports)

Sunday 25 April
12:00 Wolves v Burnley (BBC)
14:00 Leeds v Man Utd (Sky Sports)
19:00 Aston Villa v West Brom (BT Sport)

Monday 26 April
20:00 Leicester v Crystal Palace (Sky Sports)

Friday 30 April
20:00 Southampton v Leicester (Sky Sports)

Saturday 1 May
12:30 Crystal Palace v Man City (BT Sport)
15:00 Brighton v Leeds (Amazon Prime)
17:30 Chelsea v Fulham (Sky Sports)
20:00 Everton v Aston Villa (BT Sport)

Sunday 2 May
14:00 Newcastle v Arsenal (Sky Sports)
16:30 Man Utd v Liverpool (Sky Sports)
19:15 Spurs v Sheffield Utd (Sky Sports)

Monday 3 May
18:00 West Brom v Wolves (Sky Sports)
20:15 Burnley v West Ham (Sky Sports)

Friday 7 May
20:00 Leicester v Newcastle (Sky Sports)

Saturday 8 May
12:30 Leeds v Spurs (BT Sport)
15:00 Sheffield Utd v Crystal Palace (Sky Sports)
17:30 Man City v Chelsea (Sky Sports)
20:15 Liverpool v Southampton (Sky Sports)

Sunday 9 May
12:00 Wolves v Brighton (BBC)
14:05 Aston Villa v Man Utd (Sky Sports)
16:30 West Ham v Everton (Sky Sports)
19:00 Arsenal v West Brom (BT Sport)

Monday 10 May
20:00 Fulham v Burnley (Sky Sports)

Tuesday 11 May 
18:00 Man Utd v Leicester (BT Sport)
20:15 Southampton v Crystal Palace (Sky Sports)

Wednesday 12 May
20:15 Chelsea v Arsenal (Sky Sports)

Thursday 13 May 
18:00 Aston Villa v Everton (Sky Sports) 
20:15 Man Utd v Liverpool (Sky Sports)

Friday 14 May 
20:00 Newcastle v Man City (Sky Sports)

Saturday 15 May 
12:30 Burnley v Leeds (BT Sport)
15:00 Southampton v Fulham (Sky Sports)
20:00 Brighton v West Ham (Sky Sports)

Sunday 16 May
12:00 Crystal Palace v Aston Villa (Sky Sports)
14:05 Spurs v Wolves (Sky Sports)
16:30 West Brom v Liverpool (Sky Sports)
19:00 Everton v Sheff Utd (BT Sport)

Tuesday 18 May
18:00 Man Utd v Fulham (Sky Sports)
18:00 Southampton v Leeds (Sky Sports)
19:00 Brighton v Man City (BT Sport)
20:15 Chelsea v Leicester (Sky Sports)

Wednesday 19 May
18:00 Everton v Wolves (Sky Sports)
18:00 Newcastle v Sheff Utd (Sky Sports)
18:00 Spurs v Aston Villa (Sky Sports)
19:00 Crystal Palace v Arsenal (BT Sport)
20:15 Burnley v Liverpool (Sky Sports) 
20:15 West Brom v West Ham (Sky Sports)

Sunday 23 May
16:00 Arsenal v Brighton (Sky Sports Arena)
16:00 Aston Villa v Chelsea (Sky Sports Action)
16:00 Fulham v Newcastle (Sky Sports Mix)
16:00 Leeds v West Brom (BT Sport 2)
16:00 Leicester v Spurs (Sky Sports Football)
16:00 Liverpool v Crystal Palace (Sky Sports Main Event)
16:00 Man City v Everton (Sky Sports Premier League)
16:00 Sheffield Utd v Burnley (BT Sport 3)
16:00 West Ham v Southampton (Sky One)
16:00 Wolves v Man Utd (BT Sport 1)
"""

schedule_championship = """
Saturday, Sept. 12, 2020
A.F.C. Bournemouth v Blackburn Rovers
Barnsley v Luton Town
Birmingham City v Brentford
Bristol City v Coventry City
Cardiff City v Sheffield Wednesday
Derby County v Reading
Huddersfield Town v Norwich City
Millwall v Stoke City
Preston North End v Swansea City
Queens Park Rangers v Nottingham Forest
Watford v Middlesbrough
Wycombe Wanderers v Rotherham United

Saturday, Sept. 19, 2020
Blackburn Rovers v Wycombe Wanderers
Brentford v Huddersfield Town
Coventry City v Queens Park Rangers
Luton Town v Derby County
Middlesbrough v A.F.C. Bournemouth
Norwich City v Preston North End
Nottingham Forest v Cardiff City
Reading v Barnsley
Rotherham United v Millwall
Sheffield Wednesday v Watford
Stoke City v Bristol City
Swansea City v Birmingham City

Saturday, Sept. 26, 2020
A.F.C. Bournemouth v Norwich City
Barnsley v Coventry City
Birmingham City v Rotherham United
Bristol City v Sheffield Wednesday
Cardiff City v Reading
Derby County v Blackburn Rovers
Huddersfield Town v Nottingham Forest
Millwall v Brentford
Preston North End v Stoke City
Queens Park Rangers v Middlesbrough
Watford v Luton Town
Wycombe Wanderers v Swansea City

Saturday, Oct. 3, 2020
Blackburn Rovers v Cardiff City
Brentford v Preston North End
Coventry City v A.F.C. Bournemouth
Luton Town v Wycombe Wanderers
Middlesbrough v Barnsley
Norwich City v Derby County
Nottingham Forest v Bristol City
Reading v Watford
Rotherham United v Huddersfield Town
Sheffield Wednesday v Queens Park Rangers
Stoke City v Birmingham City
Swansea City v Millwall

Saturday, Oct. 17, 2020
A.F.C. Bournemouth v Queens Park Rangers
Barnsley v Bristol City
Birmingham City v Sheffield Wednesday
Blackburn Rovers v Nottingham Forest
Brentford v Coventry City
Derby County v Watford
Luton Town v Stoke City
Middlesbrough v Reading
Preston North End v Cardiff City
Rotherham United v Norwich City
Swansea City v Huddersfield Town
Wycombe Wanderers v Millwall

Tuesday, Oct. 20, 2020
Bristol City v Middlesbrough
Coventry City v Swansea City
Millwall v Luton Town
Norwich City v Birmingham City
Nottingham Forest v Rotherham United
Reading v Wycombe Wanderers

Wednesday, Oct. 21, 2020
Cardiff City v A.F.C. Bournemouth
Huddersfield Town v Derby County
Queens Park Rangers v Preston North End
Sheffield Wednesday v Brentford
Stoke City v Barnsley
Watford v Blackburn Rovers

Saturday, Oct. 24, 2020
Bristol City v Swansea City
Cardiff City v Middlesbrough
Coventry City v Blackburn Rovers
Huddersfield Town v Preston North End
Millwall v Barnsley
Norwich City v Wycombe Wanderers
Nottingham Forest v Derby County
Queens Park Rangers v Birmingham City
Reading v Rotherham United
Sheffield Wednesday v Luton Town
Stoke City v Brentford
Watford v A.F.C. Bournemouth

Tuesday, Oct. 27, 2020
Barnsley v Queens Park Rangers
Blackburn Rovers v Reading
Brentford v Norwich City
Middlesbrough v Coventry City
Swansea City v Stoke City
Wycombe Wanderers v Watford

Wednesday, Oct. 28, 2020
A.F.C. Bournemouth v Bristol City
Birmingham City v Huddersfield Town
Derby County v Cardiff City
Luton Town v Nottingham Forest
Preston North End v Millwall
Rotherham United v Sheffield Wednesday

Saturday, Oct. 31, 2020
A.F.C. Bournemouth v Derby County
Barnsley v Watford
Bristol City v Norwich City
Coventry City v Reading
Luton Town v Brentford
Middlesbrough v Nottingham Forest
Millwall v Huddersfield Town
Preston North End v Birmingham City
Queens Park Rangers v Cardiff City
Stoke City v Rotherham United
Swansea City v Blackburn Rovers
Wycombe Wanderers v Sheffield Wednesday

Tuesday, Nov. 3, 2020
Blackburn Rovers v Middlesbrough
Brentford v Swansea City
Cardiff City v Barnsley
Huddersfield Town v Bristol City
Norwich City v Millwall
Sheffield Wednesday v A.F.C. Bournemouth

Wednesday, Nov. 4, 2020
Birmingham City v Wycombe Wanderers
Derby County v Queens Park Rangers
Nottingham Forest v Coventry City
Reading v Preston North End
Rotherham United v Luton Town
Watford v Stoke City

Saturday, Nov. 7, 2020
Birmingham City v A.F.C. Bournemouth
Blackburn Rovers v Queens Park Rangers
Brentford v Middlesbrough
Cardiff City v Bristol City
Derby County v Barnsley
Huddersfield Town v Luton Town
Norwich City v Swansea City
Nottingham Forest v Wycombe Wanderers
Reading v Stoke City
Rotherham United v Preston North End
Sheffield Wednesday v Millwall
Watford v Coventry City

Saturday, Nov. 21, 2020
A.F.C. Bournemouth v Reading
Barnsley v Nottingham Forest
Bristol City v Derby County
Coventry City v Birmingham City
Luton Town v Blackburn Rovers
Middlesbrough v Norwich City
Millwall v Cardiff City
Preston North End v Sheffield Wednesday
Queens Park Rangers v Watford
Stoke City v Huddersfield Town
Swansea City v Rotherham United
Wycombe Wanderers v Brentford

Tuesday, Nov. 24, 2020
A.F.C. Bournemouth v Nottingham Forest
Barnsley v Brentford
Luton Town v Birmingham City
Preston North End v Blackburn Rovers
Queens Park Rangers v Rotherham United
Stoke City v Norwich City

Wednesday, Nov. 25, 2020
Bristol City v Watford
Coventry City v Cardiff City
Middlesbrough v Derby County
Millwall v Reading
Swansea City v Sheffield Wednesday
Wycombe Wanderers v Huddersfield Town

Saturday, Nov. 28, 2020
Birmingham City v Millwall
Blackburn Rovers v Barnsley
Brentford v Queens Park Rangers
Cardiff City v Luton Town
Derby County v Wycombe Wanderers
Huddersfield Town v Middlesbrough
Norwich City v Coventry City
Nottingham Forest v Swansea City
Reading v Bristol City
Rotherham United v A.F.C. Bournemouth
Sheffield Wednesday v Stoke City
Watford v Preston North End

Tuesday, Dec. 1, 2020
A.F.C. Bournemouth v Preston North End
Birmingham City v Barnsley
Cardiff City v Huddersfield Town
Derby County v Coventry City
Queens Park Rangers v Bristol City
Rotherham United v Brentford

Wednesday, Dec. 2, 2020
Blackburn Rovers v Millwall
Luton Town v Norwich City
Middlesbrough v Swansea City
Nottingham Forest v Watford
Sheffield Wednesday v Reading
Wycombe Wanderers v Stoke City

Saturday, Dec. 5, 2020
Barnsley v A.F.C. Bournemouth
Brentford v Blackburn Rovers
Bristol City v Birmingham City
Coventry City v Rotherham United
Huddersfield Town v Queens Park Rangers
Millwall v Derby County
Norwich City v Sheffield Wednesday
Preston North End v Wycombe Wanderers
Reading v Nottingham Forest
Stoke City v Middlesbrough
Swansea City v Luton Town
Watford v Cardiff City

Tuesday, Dec. 7, 2020
Coventry City v Luton Town
Huddersfield Town v Sheffield Wednesday
Millwall v Queens Park Rangers
Stoke City v Cardiff City
Swansea City v A.F.C. Bournemouth
Watford v Rotherham United

Wednesday, Dec. 8, 2020
Barnsley v Wycombe Wanderers
Brentford v Derby County
Bristol City v Blackburn Rovers
Norwich City v Nottingham Forest
Preston North End v Middlesbrough
Reading v Birmingham City

Saturday, Dec. 12, 2020
A.F.C. Bournemouth v Huddersfield Town
Birmingham City v Watford
Blackburn Rovers v Norwich City
Cardiff City v Swansea City
Derby County v Stoke City
Luton Town v Preston North End
Middlesbrough v Millwall
Nottingham Forest v Brentford
Queens Park Rangers v Reading
Rotherham United v Bristol City
Sheffield Wednesday v Barnsley
Wycombe Wanderers v Coventry City

Tuesday, Dec. 15, 2020
A.F.C. Bournemouth v Wycombe Wanderers
Barnsley v Preston North End
Bristol City v Millwall
Nottingham Forest v Sheffield Wednesday
Queens Park Rangers v Stoke City
Watford v Brentford

Wednesday, Dec. 16, 2020
Blackburn Rovers v Rotherham United
Cardiff City v Birmingham City
Coventry City v Huddersfield Town
Derby County v Swansea City
Middlesbrough v Luton Town
Reading v Norwich City

Saturday, Dec. 19, 2020
Birmingham City v Middlesbrough
Brentford v Reading
Huddersfield Town v Watford
Luton Town v A.F.C. Bournemouth
Millwall v Nottingham Forest
Norwich City v Cardiff City
Preston North End v Bristol City
Rotherham United v Derby County
Sheffield Wednesday v Coventry City
Stoke City v Blackburn Rovers
Swansea City v Barnsley
Wycombe Wanderers v Queens Park Rangers

Saturday, Dec. 26, 2020
A.F.C. Bournemouth v Millwall
Barnsley v Huddersfield Town
Blackburn Rovers v Sheffield Wednesday
Bristol City v Wycombe Wanderers
Cardiff City v Brentford
Coventry City v Stoke City
Derby County v Preston North End
Middlesbrough v Rotherham United
Nottingham Forest v Birmingham City
Queens Park Rangers v Swansea City
Reading v Luton Town
Watford v Norwich City

Tuesday, Dec. 29, 2020
Birmingham City v Derby County
Brentford v A.F.C. Bournemouth
Huddersfield Town v Blackburn Rovers
Luton Town v Bristol City
Millwall v Watford
Norwich City v Queens Park Rangers
Preston North End v Coventry City
Rotherham United v Barnsley
Sheffield Wednesday v Middlesbrough
Stoke City v Nottingham Forest
Swansea City v Reading
Wycombe Wanderers v Cardiff City

Saturday, Jan. 2, 2021
Birmingham City v Blackburn Rovers
Brentford v Bristol City
Huddersfield Town v Reading
Luton Town v Queens Park Rangers
Millwall v Coventry City
Norwich City v Barnsley
Preston North End v Nottingham Forest
Rotherham United v Cardiff City
Sheffield Wednesday v Derby County
Stoke City v A.F.C. Bournemouth
Swansea City v Watford
Wycombe Wanderers v Middlesbrough

Saturday, Jan. 16, 2021
A.F.C. Bournemouth v Luton Town
Barnsley v Swansea City
Blackburn Rovers v Stoke City
Bristol City v Preston North End
Cardiff City v Norwich City
Coventry City v Sheffield Wednesday
Derby County v Rotherham United
Middlesbrough v Birmingham City
Nottingham Forest v Millwall
Queens Park Rangers v Wycombe Wanderers
Reading v Brentford
Watford v Huddersfield Town

Tuesday, Jan. 19, 2021
Blackburn Rovers v Swansea City
Derby County v A.F.C. Bournemouth
Reading v Coventry City
Rotherham United v Stoke City
Sheffield Wednesday v Wycombe Wanderers
Watford v Barnsley

Wednesday, Jan. 20, 2021
Birmingham City v Preston North End
Brentford v Luton Town
Cardiff City v Queens Park Rangers
Huddersfield Town v Millwall
Norwich City v Bristol City
Nottingham Forest v Middlesbrough

Saturday, Jan. 23, 2021
A.F.C. Bournemouth v Sheffield Wednesday
Barnsley v Cardiff City
Bristol City v Huddersfield Town
Coventry City v Nottingham Forest
Luton Town v Rotherham United
Middlesbrough v Blackburn Rovers
Millwall v Norwich City
Preston North End v Reading
Queens Park Rangers v Derby County
Stoke City v Watford
Swansea City v Brentford
Wycombe Wanderers v Birmingham City

Saturday, Jan. 30, 2021
Birmingham City v Coventry City
Blackburn Rovers v Luton Town
Brentford v Wycombe Wanderers
Cardiff City v Millwall
Derby County v Bristol City
Huddersfield Town v Stoke City
Norwich City v Middlesbrough
Nottingham Forest v Barnsley
Reading v A.F.C. Bournemouth
Rotherham United v Swansea City
Sheffield Wednesday v Preston North End
Watford v Queens Park Rangers

Saturday, Feb. 6, 2021
A.F.C. Bournemouth v Birmingham City
Barnsley v Derby County
Bristol City v Cardiff City
Coventry City v Watford
Luton Town v Huddersfield Town
Middlesbrough v Brentford
Millwall v Sheffield Wednesday
Preston North End v Rotherham United
Queens Park Rangers v Blackburn Rovers
Stoke City v Reading
Swansea City v Norwich City
Wycombe Wanderers v Nottingham Forest

Saturday, Feb. 13, 2021
Birmingham City v Luton Town
Blackburn Rovers v Preston North End
Brentford v Barnsley
Cardiff City v Coventry City
Derby County v Middlesbrough
Huddersfield Town v Wycombe Wanderers
Norwich City v Stoke City
Nottingham Forest v A.F.C. Bournemouth
Reading v Millwall
Rotherham United v Queens Park Rangers
Sheffield Wednesday v Swansea City
Watford v Bristol City

Tuesday, Feb. 16, 2021
Bristol City v Reading
Luton Town v Cardiff City
Middlesbrough v Huddersfield Town
Preston North End v Watford
Stoke City v Sheffield Wednesday
Wycombe Wanderers v Derby County

Wednesday, Feb. 17, 2021
A.F.C. Bournemouth v Rotherham United
Barnsley v Blackburn Rovers
Coventry City v Norwich City
Millwall v Birmingham City
Queens Park Rangers v Brentford
Swansea City v Nottingham Forest

Saturday, Feb. 20, 2021
Bristol City v Barnsley
Cardiff City v Preston North End
Coventry City v Brentford
Huddersfield Town v Swansea City
Millwall v Wycombe Wanderers
Norwich City v Rotherham United
Nottingham Forest v Blackburn Rovers
Queens Park Rangers v A.F.C. Bournemouth
Reading v Middlesbrough
Sheffield Wednesday v Birmingham City
Stoke City v Luton Town
Watford v Derby County

Tuesday, Feb. 23, 2021
Birmingham City v Norwich City
Derby County v Huddersfield Town
Luton Town v Millwall
Middlesbrough v Bristol City
Rotherham United v Nottingham Forest
Wycombe Wanderers v Reading

Wednesday, Feb. 24, 2021
A.F.C. Bournemouth v Cardiff City
Barnsley v Stoke City
Blackburn Rovers v Watford
Brentford v Sheffield Wednesday
Preston North End v Queens Park Rangers
Swansea City v Coventry City

Saturday, Feb. 27, 2021
A.F.C. Bournemouth v Watford
Barnsley v Millwall
Birmingham City v Queens Park Rangers
Blackburn Rovers v Coventry City
Brentford v Stoke City
Derby County v Nottingham Forest
Luton Town v Sheffield Wednesday
Middlesbrough v Cardiff City
Preston North End v Huddersfield Town
Rotherham United v Reading
Swansea City v Bristol City
Wycombe Wanderers v Norwich City

Tuesday, March 2, 2021
Cardiff City v Derby County
Coventry City v Middlesbrough
Huddersfield Town v Birmingham City
Millwall v Preston North End
Nottingham Forest v Luton Town
Reading v Blackburn Rovers

Wednesday, March 3, 2021
Bristol City v A.F.C. Bournemouth
Norwich City v Brentford
Queens Park Rangers v Barnsley
Sheffield Wednesday v Rotherham United
Stoke City v Swansea City
Watford v Wycombe Wanderers

Saturday, March 6, 2021
Barnsley v Birmingham City
Brentford v Rotherham United
Bristol City v Queens Park Rangers
Coventry City v Derby County
Huddersfield Town v Cardiff City
Millwall v Blackburn Rovers
Norwich City v Luton Town
Preston North End v A.F.C. Bournemouth
Reading v Sheffield Wednesday
Stoke City v Wycombe Wanderers
Swansea City v Middlesbrough
Watford v Nottingham Forest

Saturday, March 13, 2021
A.F.C. Bournemouth v Barnsley
Birmingham City v Bristol City
Blackburn Rovers v Brentford
Cardiff City v Watford
Derby County v Millwall
Luton Town v Swansea City
Middlesbrough v Stoke City
Nottingham Forest v Reading
Queens Park Rangers v Huddersfield Town
Rotherham United v Coventry City
Sheffield Wednesday v Norwich City
Wycombe Wanderers v Preston North End

Tuesday, March 16, 2021
A.F.C. Bournemouth v Swansea City
Cardiff City v Stoke City
Derby County v Brentford
Luton Town v Coventry City
Middlesbrough v Preston North End
Rotherham United v Watford

Wednesday, March 17, 2021
Birmingham City v Reading
Blackburn Rovers v Bristol City
Nottingham Forest v Norwich City
Queens Park Rangers v Millwall
Sheffield Wednesday v Huddersfield Town
Wycombe Wanderers v Barnsley

Saturday, March 20, 2021
Barnsley v Sheffield Wednesday
Brentford v Nottingham Forest
Bristol City v Rotherham United
Coventry City v Wycombe Wanderers
Huddersfield Town v A.F.C. Bournemouth
Millwall v Middlesbrough
Norwich City v Blackburn Rovers
Preston North End v Luton Town
Reading v Queens Park Rangers
Stoke City v Derby County
Swansea City v Cardiff City
Watford v Birmingham City

Friday, April 2, 2021
A.F.C. Bournemouth v Middlesbrough
Barnsley v Reading
Birmingham City v Swansea City
Bristol City v Stoke City
Cardiff City v Nottingham Forest
Derby County v Luton Town
Huddersfield Town v Brentford
Millwall v Rotherham United
Preston North End v Norwich City
Queens Park Rangers v Coventry City
Watford v Sheffield Wednesday
Wycombe Wanderers v Blackburn Rovers

Monday, April 5, 2021
Blackburn Rovers v A.F.C. Bournemouth
Brentford v Birmingham City
Coventry City v Bristol City
Luton Town v Barnsley
Middlesbrough v Watford
Norwich City v Huddersfield Town
Nottingham Forest v Queens Park Rangers
Reading v Derby County
Rotherham United v Wycombe Wanderers
Sheffield Wednesday v Cardiff City
Stoke City v Millwall
Swansea City v Preston North End

Saturday, April 10, 2021
A.F.C. Bournemouth v Coventry City
Barnsley v Middlesbrough
Birmingham City v Stoke City
Bristol City v Nottingham Forest
Cardiff City v Blackburn Rovers
Derby County v Norwich City
Huddersfield Town v Rotherham United
Millwall v Swansea City
Preston North End v Brentford
Queens Park Rangers v Sheffield Wednesday
Watford v Reading
Wycombe Wanderers v Luton Town

Saturday, April 17, 2021
Blackburn Rovers v Derby County
Brentford v Millwall
Coventry City v Barnsley
Luton Town v Watford
Middlesbrough v Queens Park Rangers
Norwich City v A.F.C. Bournemouth
Nottingham Forest v Huddersfield Town
Reading v Cardiff City
Rotherham United v Birmingham City
Sheffield Wednesday v Bristol City
Stoke City v Preston North End
Swansea City v Wycombe Wanderers

Tuesday, April 20, 2021
Birmingham City v Nottingham Forest
Brentford v Cardiff City
Norwich City v Watford
Preston North End v Derby County
Sheffield Wednesday v Blackburn Rovers
Swansea City v Queens Park Rangers

Wednesday, April 21, 2021
Huddersfield Town v Barnsley
Luton Town v Reading
Millwall v A.F.C. Bournemouth
Rotherham United v Middlesbrough
Stoke City v Coventry City
Wycombe Wanderers v Bristol City

Saturday, April 24, 2021
A.F.C. Bournemouth v Brentford
Barnsley v Rotherham United
Blackburn Rovers v Huddersfield Town
Bristol City v Luton Town
Cardiff City v Wycombe Wanderers
Coventry City v Preston North End
Derby County v Birmingham City
Middlesbrough v Sheffield Wednesday
Nottingham Forest v Stoke City
Queens Park Rangers v Norwich City
Reading v Swansea City
Watford v Millwall

Saturday, May 1, 2021
Birmingham City v Cardiff City
Brentford v Watford
Huddersfield Town v Coventry City
Luton Town v Middlesbrough
Millwall v Bristol City
Norwich City v Reading
Preston North End v Barnsley
Rotherham United v Blackburn Rovers
Sheffield Wednesday v Nottingham Forest
Stoke City v Queens Park Rangers
Swansea City v Derby County
Wycombe Wanderers v A.F.C. Bournemouth

Saturday, May 8, 2021
A.F.C. Bournemouth v Stoke City
Barnsley v Norwich City
Blackburn Rovers v Birmingham City
Bristol City v Brentford
Cardiff City v Rotherham United
Coventry City v Millwall
Derby County v Sheffield Wednesday
Middlesbrough v Wycombe Wanderers
Nottingham Forest v Preston North End
Queens Park Rangers v Luton Town
Reading v Huddersfield Town
Watford v Swansea City
"""

schedule_leagueone = """
September:

12/09/2020 15:00 Accrington Stanley v Peterborough United

12/09/2020 15:00 Crewe Alexandra v Charlton Athletic

12/09/2020 15:00 Doncaster Rovers v Milton Keynes Dons

12/09/2020 15:00 Fleetwood Town v Burton Albion

12/09/2020 15:00 Gillingham v Hull City

12/09/2020 15:00 Ipswich Town v Wigan Athletic

12/09/2020 15:00 Lincoln City v Oxford United

12/09/2020 15:00 Northampton Town v A.F.C. Wimbledon

12/09/2020 15:00 Plymouth Argyle v Blackpool

12/09/2020 15:00 Portsmouth v Shrewsbury Town

12/09/2020 15:00 Sunderland v Bristol Rovers

12/09/2020 15:00 Swindon Town v Rochdale

19/09/2020 15:00 A.F.C. Wimbledon v Plymouth Argyle

19/09/2020 15:00 Blackpool v Swindon Town

19/09/2020 15:00 Bristol Rovers v Ipswich Town

19/09/2020 15:00 Burton Albion v Accrington Stanley

19/09/2020 15:00 Charlton Athletic v Doncaster Rovers

19/09/2020 15:00 Hull City v Crewe Alexandra

19/09/2020 15:00 Milton Keynes Dons v Lincoln City

19/09/2020 15:00 Oxford United v Sunderland

19/09/2020 15:00 Peterborough United v Fleetwood Town

19/09/2020 15:00 Rochdale v Portsmouth

19/09/2020 15:00 Shrewsbury Town v Northampton Town

19/09/2020 15:00 Wigan Athletic v Gillingham

26/09/2020 15:00 Accrington Stanley v Oxford United

26/09/2020 15:00 Crewe Alexandra v Milton Keynes Dons

26/09/2020 15:00 Doncaster Rovers v Bristol Rovers

26/09/2020 15:00 Fleetwood Town v A.F.C. Wimbledon

26/09/2020 15:00 Gillingham v Blackpool

26/09/2020 15:00 Ipswich Town v Rochdale

26/09/2020 15:00 Lincoln City v Charlton Athletic

26/09/2020 15:00 Northampton Town v Hull City

26/09/2020 15:00 Plymouth Argyle v Shrewsbury Town

26/09/2020 15:00 Portsmouth v Wigan Athletic

26/09/2020 15:00 Sunderland v Peterborough United

26/09/2020 15:00 Swindon Town v Burton Albion

October:

03/10/2020 15:00 A.F.C. Wimbledon v Accrington Stanley

03/10/2020 15:00 Blackpool v Lincoln City

03/10/2020 15:00 Bristol Rovers v Northampton Town

03/10/2020 15:00 Burton Albion v Portsmouth

03/10/2020 15:00 Charlton Athletic v Sunderland

03/10/2020 15:00 Hull City v Plymouth Argyle

03/10/2020 15:00 Milton Keynes Dons v Ipswich Town

03/10/2020 15:00 Oxford United v Crewe Alexandra

03/10/2020 15:00 Peterborough United v Swindon Town

03/10/2020 15:00 Rochdale v Fleetwood Town

03/10/2020 15:00 Shrewsbury Town v Gillingham

03/10/2020 15:00 Wigan Athletic v Doncaster Rovers

10/10/2020 15:00 Accrington Stanley v Rochdale

10/10/2020 15:00 Crewe Alexandra v Wigan Athletic

10/10/2020 15:00 Doncaster Rovers v Shrewsbury Town

10/10/2020 15:00 Fleetwood Town v Hull City

10/10/2020 15:00 Gillingham v Oxford United

10/10/2020 15:00 Ipswich Town v Charlton Athletic

10/10/2020 15:00 Lincoln City v Bristol Rovers

10/10/2020 15:00 Northampton Town v Peterborough United

10/10/2020 15:00 Plymouth Argyle v Burton Albion

10/10/2020 15:00 Portsmouth v Milton Keynes Dons

10/10/2020 15:00 Sunderland v Blackpool

10/10/2020 15:00 Swindon Town v A.F.C. Wimbledon

17/10/2020 15:00 A.F.C. Wimbledon v Shrewsbury Town

17/10/2020 15:00 Bristol Rovers v Burton Albion

17/10/2020 15:00 Charlton Athletic v Wigan Athletic

17/10/2020 15:00 Crewe Alexandra v Blackpool

17/10/2020 15:00 Fleetwood Town v Lincoln City

17/10/2020 15:00 Ipswich Town v Accrington Stanley

17/10/2020 15:00 Milton Keynes Dons v Gillingham

17/10/2020 15:00 Peterborough United v Oxford United

17/10/2020 15:00 Plymouth Argyle v Northampton Town

17/10/2020 15:00 Portsmouth v Doncaster Rovers

17/10/2020 15:00 Rochdale v Hull City

17/10/2020 15:00 Swindon Town v Sunderland

20/10/2020 19:45 Accrington Stanley v Fleetwood Town

20/10/2020 19:45 Blackpool v Charlton Athletic

20/10/2020 19:45 Burton Albion v Rochdale

20/10/2020 20:00 Doncaster Rovers v Ipswich Town

20/10/2020 19:45 Gillingham v Portsmouth

20/10/2020 19:45 Hull City v A.F.C. Wimbledon

20/10/2020 19:45 Lincoln City v Plymouth Argyle

20/10/2020 19:45 Northampton Town v Swindon Town

20/10/2020 19:45 Oxford United v Milton Keynes Dons

20/10/2020 19:45 Shrewsbury Town v Bristol Rovers

20/10/2020 19:45 Sunderland v Crewe Alexandra

20/10/2020 19:45 Wigan Athletic v Peterborough United

24/10/2020 15:00 Accrington Stanley v Bristol Rovers

24/10/2020 15:00 Blackpool v Milton Keynes Dons

24/10/2020 15:00 Burton Albion v A.F.C. Wimbledon

24/10/2020 15:00 Doncaster Rovers v Crewe Alexandra

24/10/2020 15:00 Gillingham v Fleetwood Town

24/10/2020 15:00 Hull City v Peterborough United

24/10/2020 15:00 Lincoln City v Ipswich Town

24/10/2020 15:00 Northampton Town v Charlton Athletic

24/10/2020 15:00 Oxford United v Swindon Town

24/10/2020 15:00 Shrewsbury Town v Rochdale

24/10/2020 15:00 Sunderland v Portsmouth

24/10/2020 15:00 Wigan Athletic v Plymouth Argyle

27/10/2020 19:45 A.F.C. Wimbledon v Blackpool

27/10/2020 19:45 Bristol Rovers v Hull City

27/10/2020 19:45 Charlton Athletic v Oxford United

27/10/2020 19:45 Crewe Alexandra v Lincoln City

27/10/2020 19:45 Fleetwood Town v Shrewsbury Town

27/10/2020 19:45 Ipswich Town v Gillingham

27/10/2020 19:45 Milton Keynes Dons v Wigan Athletic

27/10/2020 19:45 Peterborough United v Burton Albion

27/10/2020 19:45 Plymouth Argyle v Doncaster Rovers

27/10/2020 19:45 Portsmouth v Northampton Town

27/10/2020 19:45 Rochdale v Sunderland

27/10/2020 19:45 Swindon Town v Accrington Stanley

31/10/2020 15:00 Accrington Stanley v Plymouth Argyle

31/10/2020 15:00 Burton Albion v Blackpool

31/10/2020 15:00 Doncaster Rovers v Lincoln City

31/10/2020 15:00 Fleetwood Town v Oxford United

31/10/2020 15:00 Gillingham v Sunderland

31/10/2020 15:00 Ipswich Town v Crewe Alexandra

31/10/2020 15:00 Milton Keynes Dons v A.F.C. Wimbledon

31/10/2020 15:00 Peterborough United v Shrewsbury Town

31/10/2020 15:00 Portsmouth v Charlton Athletic

31/10/2020 15:00 Rochdale v Bristol Rovers

31/10/2020 15:00 Swindon Town v Hull City

31/10/2020 15:00 Wigan Athletic v Northampton Town

November:

03/11/2020 19:45 A.F.C. Wimbledon v Doncaster Rovers

03/11/2020 19:45 Blackpool v Wigan Athletic

03/11/2020 19:45 Bristol Rovers v Peterborough United

03/11/2020 19:45 Charlton Athletic v Fleetwood Town

03/11/2020 19:45 Crewe Alexandra v Gillingham

03/11/2020 19:45 Hull City v Accrington Stanley

03/11/2020 19:45 Lincoln City v Portsmouth

03/11/2020 19:45 Northampton Town v Milton Keynes Dons

03/11/2020 19:45 Oxford United v Rochdale

03/11/2020 19:45 Plymouth Argyle v Swindon Town

03/11/2020 19:45 Shrewsbury Town v Burton Albion

03/11/2020 19:45 Sunderland v Ipswich Town

14/11/2020 15:00 A.F.C. Wimbledon v Wigan Athletic

14/11/2020 15:00 Blackpool v Ipswich Town

14/11/2020 15:00 Bristol Rovers v Fleetwood Town

14/11/2020 15:00 Charlton Athletic v Rochdale

14/11/2020 15:00 Crewe Alexandra v Peterborough United

14/11/2020 15:00 Hull City v Burton Albion

14/11/2020 15:00 Lincoln City v Gillingham

14/11/2020 15:00 Northampton Town v Accrington Stanley

14/11/2020 15:00 Oxford United v Doncaster Rovers

14/11/2020 15:00 Plymouth Argyle v Portsmouth

14/11/2020 15:00 Shrewsbury Town v Swindon Town

14/11/2020 15:00 Sunderland v Milton Keynes Dons

21/11/2020 15:00 Accrington Stanley v Lincoln City

21/11/2020 15:00 Burton Albion v Northampton Town

21/11/2020 15:00 Doncaster Rovers v Sunderland

21/11/2020 15:00 Fleetwood Town v Plymouth Argyle

21/11/2020 15:00 Gillingham v Charlton Athletic

21/11/2020 15:00 Ipswich Town v Shrewsbury Town

21/11/2020 15:00 Milton Keynes Dons v Hull City

21/11/2020 15:00 Peterborough United v Blackpool

21/11/2020 15:00 Portsmouth v Crewe Alexandra

21/11/2020 15:00 Rochdale v A.F.C. Wimbledon

21/11/2020 15:00 Swindon Town v Bristol Rovers

21/11/2020 15:00 Wigan Athletic v Oxford United

24/11/2020 19:45 Accrington Stanley v Crewe Alexandra

24/11/2020 19:45 Burton Albion v Charlton Athletic

24/11/2020 20:00 Doncaster Rovers v Blackpool

24/11/2020 19:45 Fleetwood Town v Sunderland

24/11/2020 19:45 Gillingham v A.F.C. Wimbledon

24/11/2020 19:45 Ipswich Town v Hull City

24/11/2020 19:45 Milton Keynes Dons v Shrewsbury Town

24/11/2020 19:45 Peterborough United v Plymouth Argyle

24/11/2020 19:45 Portsmouth v Oxford United

24/11/2020 19:45 Rochdale v Northampton Town

24/11/2020 19:45 Swindon Town v Lincoln City

24/11/2020 19:45 Wigan Athletic v Bristol Rovers

RELATED ARTICLES

Ismaila Sarr teases Liverpool move with Reds keen on Watford ace

Leeds Premier League fixtures 2020/21: Key dates and full schedule
December:

01/12/2020 19:45 A.F.C. Wimbledon v Peterborough United

01/12/2020 19:45 Blackpool v Portsmouth

01/12/2020 19:45 Bristol Rovers v Gillingham

01/12/2020 19:45 Charlton Athletic v Milton Keynes Dons

01/12/2020 19:45 Crewe Alexandra v Swindon Town

01/12/2020 19:45 Hull City v Doncaster Rovers

01/12/2020 19:45 Lincoln City v Wigan Athletic

01/12/2020 19:45 Northampton Town v Fleetwood Town

01/12/2020 19:45 Oxford United v Ipswich Town

01/12/2020 19:45 Plymouth Argyle v Rochdale

01/12/2020 19:45 Shrewsbury Town v Accrington Stanley

01/12/2020 19:45 Sunderland v Burton Albion

05/12/2020 15:00 A.F.C. Wimbledon v Bristol Rovers

05/12/2020 15:00 Accrington Stanley v Milton Keynes Dons

05/12/2020 15:00 Burton Albion v Crewe Alexandra

05/12/2020 15:00 Fleetwood Town v Blackpool

05/12/2020 15:00 Gillingham v Swindon Town

05/12/2020 15:00 Northampton Town v Doncaster Rovers

05/12/2020 15:00 Oxford United v Hull City

05/12/2020 15:00 Plymouth Argyle v Ipswich Town

05/12/2020 15:00 Portsmouth v Peterborough United

05/12/2020 15:00 Rochdale v Lincoln City

05/12/2020 15:00 Shrewsbury Town v Charlton Athletic

05/12/2020 15:00 Sunderland v Wigan Athletic

12/12/2020 15:00 Blackpool v Oxford United

12/12/2020 15:00 Bristol Rovers v Plymouth Argyle

12/12/2020 15:00 Charlton Athletic v A.F.C. Wimbledon

12/12/2020 15:00 Crewe Alexandra v Northampton Town

12/12/2020 15:00 Doncaster Rovers v Gillingham

12/12/2020 15:00 Hull City v Shrewsbury Town

12/12/2020 15:00 Ipswich Town v Portsmouth

12/12/2020 15:00 Lincoln City v Sunderland

12/12/2020 15:00 Milton Keynes Dons v Burton Albion

12/12/2020 15:00 Peterborough United v Rochdale

12/12/2020 15:00 Swindon Town v Fleetwood Town

12/12/2020 15:00 Wigan Athletic v Accrington Stanley

15/12/2020 19:45 Blackpool v Hull City

15/12/2020 19:45 Charlton Athletic v Bristol Rovers

15/12/2020 19:45 Crewe Alexandra v Plymouth Argyle

15/12/2020 20:00 Doncaster Rovers v Swindon Town

15/12/2020 19:45 Gillingham v Accrington Stanley

15/12/2020 19:45 Ipswich Town v Burton Albion

15/12/2020 19:45 Lincoln City v Shrewsbury Town

15/12/2020 19:45 Milton Keynes Dons v Peterborough United

15/12/2020 19:45 Oxford United v Northampton Town

15/12/2020 19:45 Portsmouth v Fleetwood Town

15/12/2020 19:45 Sunderland v A.F.C. Wimbledon

15/12/2020 19:45 Wigan Athletic v Rochdale

19/12/2020 15:00 A.F.C. Wimbledon v Crewe Alexandra

19/12/2020 15:00 Accrington Stanley v Blackpool

19/12/2020 15:00 Bristol Rovers v Oxford United

19/12/2020 15:00 Burton Albion v Doncaster Rovers

19/12/2020 15:00 Fleetwood Town v Wigan Athletic

19/12/2020 15:00 Hull City v Portsmouth

19/12/2020 15:00 Northampton Town v Lincoln City

19/12/2020 15:00 Peterborough United v Ipswich Town

19/12/2020 15:00 Plymouth Argyle v Milton Keynes Dons

19/12/2020 15:00 Rochdale v Gillingham

19/12/2020 15:00 Shrewsbury Town v Sunderland

19/12/2020 15:00 Swindon Town v Charlton Athletic

26/12/2020 15:00 Blackpool v Rochdale

26/12/2020 15:00 Charlton Athletic v Plymouth Argyle

26/12/2020 15:00 Crewe Alexandra v Fleetwood Town

26/12/2020 15:00 Doncaster Rovers v Accrington Stanley

26/12/2020 15:00 Gillingham v Peterborough United

26/12/2020 15:00 Ipswich Town v Northampton Town

26/12/2020 15:00 Lincoln City v Burton Albion

26/12/2020 15:00 Milton Keynes Dons v Bristol Rovers

26/12/2020 15:00 Oxford United v A.F.C. Wimbledon

26/12/2020 15:00 Portsmouth v Swindon Town

26/12/2020 15:00 Sunderland v Hull City

26/12/2020 15:00 Wigan Athletic v Shrewsbury Town

29/12/2020 19:45 A.F.C. Wimbledon v Ipswich Town

29/12/2020 19:45 Accrington Stanley v Sunderland

29/12/2020 19:45 Bristol Rovers v Portsmouth

29/12/2020 19:45 Burton Albion v Wigan Athletic

29/12/2020 19:45 Fleetwood Town v Doncaster Rovers

29/12/2020 19:45 Hull City v Lincoln City

29/12/2020 19:45 Northampton Town v Gillingham

29/12/2020 19:45 Peterborough United v Charlton Athletic

29/12/2020 19:45 Plymouth Argyle v Oxford United

29/12/2020 19:45 Rochdale v Crewe Alexandra

29/12/2020 19:45 Shrewsbury Town v Blackpool

29/12/2020 19:45 Swindon Town v Milton Keynes Dons

January:

02/01/2021 15:00 A.F.C. Wimbledon v Lincoln City

02/01/2021 15:00 Accrington Stanley v Portsmouth

02/01/2021 15:00 Bristol Rovers v Blackpool

02/01/2021 15:00 Burton Albion v Oxford United

02/01/2021 15:00 Fleetwood Town v Ipswich Town

02/01/2021 15:00 Hull City v Charlton Athletic

02/01/2021 15:00 Northampton Town v Sunderland

02/01/2021 15:00 Peterborough United v Doncaster Rovers

02/01/2021 15:00 Plymouth Argyle v Gillingham

02/01/2021 15:00 Rochdale v Milton Keynes Dons

02/01/2021 15:00 Shrewsbury Town v Crewe Alexandra

02/01/2021 15:00 Swindon Town v Wigan Athletic

09/01/2021 15:00 Blackpool v Northampton Town

09/01/2021 15:00 Charlton Athletic v Accrington Stanley

09/01/2021 15:00 Crewe Alexandra v Bristol Rovers

09/01/2021 15:00 Doncaster Rovers v Rochdale

09/01/2021 15:00 Gillingham v Burton Albion

09/01/2021 15:00 Ipswich Town v Swindon Town

09/01/2021 15:00 Lincoln City v Peterborough United

09/01/2021 15:00 Milton Keynes Dons v Fleetwood Town

09/01/2021 15:00 Oxford United v Shrewsbury Town

09/01/2021 15:00 Portsmouth v A.F.C. Wimbledon

09/01/2021 15:00 Sunderland v Plymouth Argyle

09/01/2021 15:00 Wigan Athletic v Hull City

16/01/2021 15:00 A.F.C. Wimbledon v Sunderland

16/01/2021 15:00 Accrington Stanley v Gillingham

16/01/2021 15:00 Bristol Rovers v Charlton Athletic

16/01/2021 15:00 Burton Albion v Ipswich Town

16/01/2021 15:00 Fleetwood Town v Portsmouth

16/01/2021 15:00 Hull City v Blackpool

16/01/2021 15:00 Northampton Town v Oxford United

16/01/2021 15:00 Peterborough United v Milton Keynes Dons

16/01/2021 15:00 Plymouth Argyle v Crewe Alexandra

16/01/2021 15:00 Rochdale v Wigan Athletic

16/01/2021 15:00 Shrewsbury Town v Lincoln City

16/01/2021 15:00 Swindon Town v Doncaster Rovers

23/01/2021 15:00 Blackpool v Accrington Stanley

23/01/2021 15:00 Charlton Athletic v Swindon Town

23/01/2021 15:00 Crewe Alexandra v A.F.C. Wimbledon

23/01/2021 15:00 Doncaster Rovers v Burton Albion

23/01/2021 15:00 Gillingham v Rochdale

23/01/2021 15:00 Ipswich Town v Peterborough United

23/01/2021 15:00 Lincoln City v Northampton Town

23/01/2021 15:00 Milton Keynes Dons v Plymouth Argyle

23/01/2021 15:00 Oxford United v Bristol Rovers

23/01/2021 15:00 Portsmouth v Hull City

23/01/2021 15:00 Sunderland v Shrewsbury Town

23/01/2021 15:00 Wigan Athletic v Fleetwood Town

26/01/2021 19:45 Accrington Stanley v Hull City

26/01/2021 19:45 Burton Albion v Shrewsbury Town

26/01/2021 20:00 Doncaster Rovers v A.F.C. Wimbledon

26/01/2021 19:45 Fleetwood Town v Northampton Town

26/01/2021 19:45 Gillingham v Crewe Alexandra

26/01/2021 19:45 Ipswich Town v Sunderland

26/01/2021 19:45 Milton Keynes Dons v Charlton Athletic

26/01/2021 19:45 Peterborough United v Bristol Rovers

26/01/2021 19:45 Portsmouth v Lincoln City

26/01/2021 19:45 Rochdale v Oxford United

26/01/2021 19:45 Swindon Town v Plymouth Argyle

26/01/2021 19:45 Wigan Athletic v Blackpool

30/01/2021 15:00 A.F.C. Wimbledon v Milton Keynes Dons

30/01/2021 15:00 Blackpool v Burton Albion

30/01/2021 15:00 Bristol Rovers v Rochdale

30/01/2021 15:00 Charlton Athletic v Portsmouth

30/01/2021 15:00 Crewe Alexandra v Ipswich Town

30/01/2021 15:00 Hull City v Swindon Town

30/01/2021 15:00 Lincoln City v Doncaster Rovers

30/01/2021 15:00 Northampton Town v Wigan Athletic

30/01/2021 15:00 Oxford United v Fleetwood Town

30/01/2021 15:00 Plymouth Argyle v Accrington Stanley

30/01/2021 15:00 Shrewsbury Town v Peterborough United

30/01/2021 15:00 Sunderland v Gillingham

February:

06/02/2021 15:00 Accrington Stanley v Northampton Town

06/02/2021 15:00 Burton Albion v Hull City

06/02/2021 15:00 Doncaster Rovers v Oxford United

06/02/2021 15:00 Fleetwood Town v Bristol Rovers

06/02/2021 15:00 Gillingham v Lincoln City

06/02/2021 15:00 Ipswich Town v Blackpool

06/02/2021 15:00 Milton Keynes Dons v Sunderland

06/02/2021 15:00 Peterborough United v Crewe Alexandra

06/02/2021 15:00 Portsmouth v Plymouth Argyle

06/02/2021 15:00 Rochdale v Charlton Athletic

06/02/2021 15:00 Swindon Town v Shrewsbury Town

06/02/2021 15:00 Wigan Athletic v A.F.C. Wimbledon

13/02/2021 15:00 A.F.C. Wimbledon v Rochdale

13/02/2021 15:00 Blackpool v Peterborough United

13/02/2021 15:00 Bristol Rovers v Swindon Town

13/02/2021 15:00 Charlton Athletic v Gillingham

13/02/2021 15:00 Crewe Alexandra v Portsmouth

13/02/2021 15:00 Hull City v Milton Keynes Dons

13/02/2021 15:00 Lincoln City v Accrington Stanley

13/02/2021 15:00 Northampton Town v Burton Albion

13/02/2021 15:00 Oxford United v Wigan Athletic

13/02/2021 15:00 Plymouth Argyle v Fleetwood Town

13/02/2021 15:00 Shrewsbury Town v Ipswich Town

13/02/2021 15:00 Sunderland v Doncaster Rovers

20/02/2021 15:00 Accrington Stanley v Shrewsbury Town

20/02/2021 15:00 Burton Albion v Sunderland

20/02/2021 15:00 Doncaster Rovers v Hull City

20/02/2021 15:00 Fleetwood Town v Charlton Athletic

20/02/2021 15:00 Gillingham v Bristol Rovers

20/02/2021 15:00 Ipswich Town v Oxford United

20/02/2021 15:00 Milton Keynes Dons v Northampton Town

20/02/2021 15:00 Peterborough United v A.F.C. Wimbledon

20/02/2021 15:00 Portsmouth v Blackpool

20/02/2021 15:00 Rochdale v Plymouth Argyle

20/02/2021 15:00 Swindon Town v Crewe Alexandra

20/02/2021 15:00 Wigan Athletic v Lincoln City

23/02/2021 19:45 A.F.C. Wimbledon v Gillingham

23/02/2021 19:45 Blackpool v Doncaster Rovers

23/02/2021 19:45 Bristol Rovers v Wigan Athletic

23/02/2021 19:45 Charlton Athletic v Burton Albion

23/02/2021 19:45 Crewe Alexandra v Accrington Stanley

23/02/2021 19:45 Hull City v Ipswich Town

23/02/2021 19:45 Lincoln City v Swindon Town

23/02/2021 19:45 Northampton Town v Rochdale

23/02/2021 19:45 Oxford United v Portsmouth

23/02/2021 19:45 Plymouth Argyle v Peterborough United

23/02/2021 19:45 Shrewsbury Town v Milton Keynes Dons

23/02/2021 19:45 Sunderland v Fleetwood Town

27/02/2021 15:00 A.F.C. Wimbledon v Hull City

27/02/2021 15:00 Bristol Rovers v Shrewsbury Town

27/02/2021 15:00 Charlton Athletic v Blackpool

27/02/2021 15:00 Crewe Alexandra v Sunderland

27/02/2021 15:00 Fleetwood Town v Accrington Stanley

27/02/2021 15:00 Ipswich Town v Doncaster Rovers

27/02/2021 15:00 Milton Keynes Dons v Oxford United

27/02/2021 15:00 Peterborough United v Wigan Athletic

27/02/2021 15:00 Plymouth Argyle v Lincoln City

27/02/2021 15:00 Portsmouth v Gillingham

27/02/2021 15:00 Rochdale v Burton Albion

27/02/2021 15:00 Swindon Town v Northampton Town

EFL fixtures

EFL fixtures 2020/21 in full (Image: GETTY)
March:

02/03/2021 19:45 Accrington Stanley v Ipswich Town

02/03/2021 19:45 Blackpool v Crewe Alexandra

02/03/2021 19:45 Burton Albion v Bristol Rovers

02/03/2021 20:00 Doncaster Rovers v Portsmouth

02/03/2021 19:45 Gillingham v Milton Keynes Dons

02/03/2021 19:45 Hull City v Rochdale

02/03/2021 19:45 Lincoln City v Fleetwood Town

02/03/2021 19:45 Northampton Town v Plymouth Argyle

02/03/2021 19:45 Oxford United v Peterborough United

02/03/2021 19:45 Shrewsbury Town v A.F.C. Wimbledon

02/03/2021 19:45 Sunderland v Swindon Town

02/03/2021 19:45 Wigan Athletic v Charlton Athletic

06/03/2021 15:00 Accrington Stanley v Swindon Town

06/03/2021 15:00 Blackpool v A.F.C. Wimbledon

06/03/2021 15:00 Burton Albion v Peterborough United

06/03/2021 15:00 Doncaster Rovers v Plymouth Argyle

06/03/2021 15:00 Gillingham v Ipswich Town

06/03/2021 15:00 Hull City v Bristol Rovers

06/03/2021 15:00 Lincoln City v Crewe Alexandra

06/03/2021 15:00 Northampton Town v Portsmouth

06/03/2021 15:00 Oxford United v Charlton Athletic

06/03/2021 15:00 Shrewsbury Town v Fleetwood Town

06/03/2021 15:00 Sunderland v Rochdale

06/03/2021 15:00 Wigan Athletic v Milton Keynes Dons

09/03/2021 19:45 A.F.C. Wimbledon v Burton Albion

09/03/2021 19:45 Bristol Rovers v Accrington Stanley

09/03/2021 19:45 Charlton Athletic v Northampton Town

09/03/2021 19:45 Crewe Alexandra v Doncaster Rovers

09/03/2021 19:45 Fleetwood Town v Gillingham

09/03/2021 19:45 Ipswich Town v Lincoln City

09/03/2021 19:45 Milton Keynes Dons v Blackpool

09/03/2021 19:45 Peterborough United v Hull City

09/03/2021 19:45 Plymouth Argyle v Wigan Athletic

09/03/2021 19:45 Portsmouth v Sunderland

09/03/2021 19:45 Rochdale v Shrewsbury Town

09/03/2021 19:45 Swindon Town v Oxford United

13/03/2021 15:00 Blackpool v Fleetwood Town

13/03/2021 15:00 Bristol Rovers v A.F.C. Wimbledon

13/03/2021 15:00 Charlton Athletic v Shrewsbury Town

13/03/2021 15:00 Crewe Alexandra v Burton Albion

13/03/2021 15:00 Doncaster Rovers v Northampton Town

13/03/2021 15:00 Hull City v Oxford United

13/03/2021 15:00 Ipswich Town v Plymouth Argyle

13/03/2021 15:00 Lincoln City v Rochdale

13/03/2021 15:00 Milton Keynes Dons v Accrington Stanley

13/03/2021 15:00 Peterborough United v Portsmouth

13/03/2021 15:00 Swindon Town v Gillingham

13/03/2021 15:00 Wigan Athletic v Sunderland

20/03/2021 15:00 A.F.C. Wimbledon v Charlton Athletic

20/03/2021 15:00 Accrington Stanley v Wigan Athletic

20/03/2021 15:00 Burton Albion v Milton Keynes Dons

20/03/2021 15:00 Fleetwood Town v Swindon Town

20/03/2021 15:00 Gillingham v Doncaster Rovers

20/03/2021 15:00 Northampton Town v Crewe Alexandra

20/03/2021 15:00 Oxford United v Blackpool

20/03/2021 15:00 Plymouth Argyle v Bristol Rovers

20/03/2021 15:00 Portsmouth v Ipswich Town

20/03/2021 15:00 Rochdale v Peterborough United

20/03/2021 15:00 Shrewsbury Town v Hull City

20/03/2021 15:00 Sunderland v Lincoln City

27/03/2021 15:00 A.F.C. Wimbledon v Northampton Town

27/03/2021 15:00 Blackpool v Plymouth Argyle

27/03/2021 15:00 Bristol Rovers v Sunderland

27/03/2021 15:00 Burton Albion v Fleetwood Town

27/03/2021 15:00 Charlton Athletic v Crewe Alexandra

27/03/2021 15:00 Hull City v Gillingham

27/03/2021 15:00 Milton Keynes Dons v Doncaster Rovers

27/03/2021 15:00 Oxford United v Lincoln City

27/03/2021 15:00 Peterborough United v Accrington Stanley

27/03/2021 15:00 Rochdale v Swindon Town

27/03/2021 15:00 Shrewsbury Town v Portsmouth

27/03/2021 15:00 Wigan Athletic v Ipswich Town

April:

02/04/2021 15:00 Accrington Stanley v Burton Albion

02/04/2021 15:00 Crewe Alexandra v Hull City

02/04/2021 15:00 Doncaster Rovers v Charlton Athletic

02/04/2021 15:00 Fleetwood Town v Peterborough United

02/04/2021 15:00 Gillingham v Wigan Athletic

02/04/2021 15:00 Ipswich Town v Bristol Rovers

02/04/2021 15:00 Lincoln City v Milton Keynes Dons

02/04/2021 15:00 Northampton Town v Shrewsbury Town

02/04/2021 15:00 Plymouth Argyle v A.F.C. Wimbledon

02/04/2021 15:00 Portsmouth v Rochdale

02/04/2021 15:00 Sunderland v Oxford United

02/04/2021 15:00 Swindon Town v Blackpool

05/04/2021 15:00 A.F.C. Wimbledon v Fleetwood Town

05/04/2021 15:00 Blackpool v Gillingham

05/04/2021 15:00 Bristol Rovers v Doncaster Rovers

05/04/2021 15:00 Burton Albion v Swindon Town

05/04/2021 15:00 Charlton Athletic v Lincoln City

05/04/2021 15:00 Hull City v Northampton Town

05/04/2021 15:00 Milton Keynes Dons v Crewe Alexandra

05/04/2021 15:00 Oxford United v Accrington Stanley

05/04/2021 15:00 Peterborough United v Sunderland

05/04/2021 15:00 Rochdale v Ipswich Town

05/04/2021 15:00 Shrewsbury Town v Plymouth Argyle

05/04/2021 15:00 Wigan Athletic v Portsmouth

10/04/2021 15:00 Accrington Stanley v A.F.C. Wimbledon

10/04/2021 15:00 Crewe Alexandra v Oxford United

10/04/2021 15:00 Doncaster Rovers v Wigan Athletic

10/04/2021 15:00 Fleetwood Town v Rochdale

10/04/2021 15:00 Gillingham v Shrewsbury Town

10/04/2021 15:00 Ipswich Town v Milton Keynes Dons

10/04/2021 15:00 Lincoln City v Blackpool

10/04/2021 15:00 Northampton Town v Bristol Rovers

10/04/2021 15:00 Plymouth Argyle v Hull City

10/04/2021 15:00 Portsmouth v Burton Albion

10/04/2021 15:00 Sunderland v Charlton Athletic

10/04/2021 15:00 Swindon Town v Peterborough United

17/04/2021 15:00 A.F.C. Wimbledon v Swindon Town

17/04/2021 15:00 Blackpool v Sunderland

17/04/2021 15:00 Bristol Rovers v Lincoln City

17/04/2021 15:00 Burton Albion v Plymouth Argyle

17/04/2021 15:00 Charlton Athletic v Ipswich Town

17/04/2021 15:00 Hull City v Fleetwood Town

17/04/2021 15:00 Milton Keynes Dons v Portsmouth

17/04/2021 15:00 Oxford United v Gillingham

17/04/2021 15:00 Peterborough United v Northampton Town

17/04/2021 15:00 Rochdale v Accrington Stanley

17/04/2021 15:00 Shrewsbury Town v Doncaster Rovers

17/04/2021 15:00 Wigan Athletic v Crewe Alexandra

20/04/2021 19:45 A.F.C. Wimbledon v Oxford United

20/04/2021 19:45 Accrington Stanley v Doncaster Rovers

20/04/2021 19:45 Bristol Rovers v Milton Keynes Dons

20/04/2021 19:45 Burton Albion v Lincoln City

20/04/2021 19:45 Fleetwood Town v Crewe Alexandra

20/04/2021 19:45 Hull City v Sunderland

20/04/2021 19:45 Northampton Town v Ipswich Town

20/04/2021 19:45 Peterborough United v Gillingham

20/04/2021 19:45 Plymouth Argyle v Charlton Athletic

20/04/2021 19:45 Rochdale v Blackpool

20/04/2021 19:45 Shrewsbury Town v Wigan Athletic

20/04/2021 19:45 Swindon Town v Portsmouth

24/04/2021 15:00 Blackpool v Shrewsbury Town

24/04/2021 15:00 Charlton Athletic v Peterborough United

24/04/2021 15:00 Crewe Alexandra v Rochdale

24/04/2021 15:00 Doncaster Rovers v Fleetwood Town

24/04/2021 15:00 Gillingham v Northampton Town

24/04/2021 15:00 Ipswich Town v A.F.C. Wimbledon

24/04/2021 15:00 Lincoln City v Hull City

24/04/2021 15:00 Milton Keynes Dons v Swindon Town

24/04/2021 15:00 Oxford United v Plymouth Argyle

24/04/2021 15:00 Portsmouth v Bristol Rovers

24/04/2021 15:00 Sunderland v Accrington Stanley

24/04/2021 15:00 Wigan Athletic v Burton Albion

May:

01/05/2021 15:00 A.F.C. Wimbledon v Portsmouth

01/05/2021 15:00 Accrington Stanley v Charlton Athletic

01/05/2021 15:00 Bristol Rovers v Crewe Alexandra

01/05/2021 15:00 Burton Albion v Gillingham

01/05/2021 15:00 Fleetwood Town v Milton Keynes Dons

01/05/2021 15:00 Hull City v Wigan Athletic

01/05/2021 15:00 Northampton Town v Blackpool

01/05/2021 15:00 Peterborough United v Lincoln City

01/05/2021 15:00 Plymouth Argyle v Sunderland

01/05/2021 15:00 Rochdale v Doncaster Rovers

01/05/2021 15:00 Shrewsbury Town v Oxford United

01/05/2021 15:00 Swindon Town v Ipswich Town

08/05/2021 15:00 Blackpool v Bristol Rovers

08/05/2021 15:00 Charlton Athletic v Hull City

08/05/2021 15:00 Crewe Alexandra v Shrewsbury Town

08/05/2021 15:00 Doncaster Rovers v Peterborough United

08/05/2021 15:00 Gillingham v Plymouth Argyle

08/05/2021 15:00 Ipswich Town v Fleetwood Town

08/05/2021 15:00 Lincoln City v A.F.C. Wimbledon

08/05/2021 15:00 Milton Keynes Dons v Rochdale

08/05/2021 15:00 Oxford United v Burton Albion

08/05/2021 15:00 Portsmouth v Accrington Stanley

08/05/2021 15:00 Sunderland v Northampton Town

08/05/2021 15:00 Wigan Athletic v Swindon Town
"""

schedule_leaguetwo = """
September:

12/09/2020 15:00 Barrow v Stevenage

12/09/2020 15:00 Bolton Wanderers v Forest Green Rovers

12/09/2020 15:00 Bradford City v Colchester United

12/09/2020 15:00 Cambridge United v Carlisle United

12/09/2020 15:00 Cheltenham Town v Morecambe

12/09/2020 15:00 Mansfield Town v Tranmere Rovers

12/09/2020 15:00 Oldham Athletic v Leyton Orient

12/09/2020 15:00 Port Vale v Crawley Town

12/09/2020 15:00 Salford City v Exeter City

12/09/2020 15:00 Scunthorpe United v Newport County

12/09/2020 15:00 Southend United v Harrogate Town

12/09/2020 15:00 Walsall v Grimsby Town

19/09/2020 15:00 Carlisle United v Southend United

19/09/2020 15:00 Colchester United v Bolton Wanderers

19/09/2020 15:00 Crawley Town v Scunthorpe United

19/09/2020 15:00 Exeter City v Port Vale

19/09/2020 15:00 Forest Green Rovers v Bradford City

19/09/2020 15:00 Grimsby Town v Salford City

19/09/2020 15:00 Harrogate Town v Walsall

19/09/2020 15:00 Leyton Orient v Mansfield Town

19/09/2020 15:00 Morecambe v Cambridge United

19/09/2020 15:00 Newport County v Barrow

19/09/2020 15:00 Stevenage v Oldham Athletic

19/09/2020 15:00 Tranmere Rovers v Cheltenham Town

26/09/2020 15:00 Barrow v Colchester United

26/09/2020 15:00 Bolton Wanderers v Newport County

26/09/2020 15:00 Bradford City v Stevenage

26/09/2020 15:00 Cambridge United v Tranmere Rovers

26/09/2020 15:00 Cheltenham Town v Grimsby Town

26/09/2020 15:00 Mansfield Town v Exeter City

26/09/2020 15:00 Oldham Athletic v Crawley Town

26/09/2020 15:00 Port Vale v Harrogate Town

26/09/2020 15:00 Salford City v Forest Green Rovers

26/09/2020 15:00 Scunthorpe United v Carlisle United

26/09/2020 15:00 Southend United v Morecambe

26/09/2020 15:00 Walsall v Leyton Orient

October:

03/10/2020 15:00 Carlisle United v Barrow

03/10/2020 15:00 Colchester United v Oldham Athletic

03/10/2020 15:00 Crawley Town v Southend United

03/10/2020 15:00 Exeter City v Cambridge United

03/10/2020 15:00 Forest Green Rovers v Walsall

03/10/2020 15:00 Grimsby Town v Bradford City

03/10/2020 15:00 Harrogate Town v Bolton Wanderers

03/10/2020 15:00 Leyton Orient v Cheltenham Town

03/10/2020 15:00 Morecambe v Port Vale

03/10/2020 15:00 Newport County v Mansfield Town

03/10/2020 15:00 Stevenage v Salford City

03/10/2020 15:00 Tranmere Rovers v Scunthorpe United

10/10/2020 15:00 Barrow v Leyton Orient

10/10/2020 15:00 Bolton Wanderers v Grimsby Town

10/10/2020 15:00 Bradford City v Harrogate Town

10/10/2020 15:00 Cambridge United v Newport County

10/10/2020 15:00 Cheltenham Town v Crawley Town

10/10/2020 15:00 Mansfield Town v Stevenage

10/10/2020 15:00 Oldham Athletic v Morecambe

10/10/2020 15:00 Port Vale v Carlisle United

10/10/2020 15:00 Salford City v Tranmere Rovers

10/10/2020 15:00 Scunthorpe United v Forest Green Rovers

10/10/2020 15:00 Southend United v Exeter City

10/10/2020 15:00 Walsall v Colchester United

17/10/2020 15:00 Bolton Wanderers v Oldham Athletic

17/10/2020 15:00 Carlisle United v Colchester United

17/10/2020 15:00 Crawley Town v Morecambe

17/10/2020 15:00 Forest Green Rovers v Stevenage

17/10/2020 15:00 Harrogate Town v Barrow

17/10/2020 15:00 Leyton Orient v Grimsby Town

17/10/2020 15:00 Mansfield Town v Bradford City

17/10/2020 15:00 Newport County v Tranmere Rovers

17/10/2020 15:00 Port Vale v Salford City

17/10/2020 15:00 Scunthorpe United v Cambridge United

17/10/2020 15:00 Southend United v Cheltenham Town

17/10/2020 15:00 Walsall v Exeter City

20/10/2020 19:45 Barrow v Bolton Wanderers

20/10/2020 19:45 Bradford City v Walsall

20/10/2020 19:45 Cambridge United v Port Vale

20/10/2020 19:45 Cheltenham Town v Scunthorpe United

20/10/2020 19:45 Colchester United v Forest Green Rovers

20/10/2020 19:45 Exeter City v Crawley Town

20/10/2020 19:45 Grimsby Town v Harrogate Town

20/10/2020 19:45 Morecambe v Mansfield Town

20/10/2020 19:45 Oldham Athletic v Carlisle United

20/10/2020 19:45 Salford City v Southend United

20/10/2020 19:45 Stevenage v Newport County

20/10/2020 19:45 Tranmere Rovers v Leyton Orient

24/10/2020 15:00 Barrow v Walsall

24/10/2020 15:00 Bradford City v Newport County

24/10/2020 15:00 Cambridge United v Bolton Wanderers

24/10/2020 15:00 Cheltenham Town v Mansfield Town

24/10/2020 15:00 Colchester United v Harrogate Town

24/10/2020 15:00 Exeter City v Scunthorpe United

24/10/2020 15:00 Grimsby Town v Carlisle United

24/10/2020 15:00 Morecambe v Forest Green Rovers

24/10/2020 15:00 Oldham Athletic v Port Vale

24/10/2020 15:00 Salford City v Crawley Town

24/10/2020 15:00 Stevenage v Leyton Orient

24/10/2020 15:00 Tranmere Rovers v Southend United

27/10/2020 20:00 Bolton Wanderers v Bradford City

27/10/2020 19:45 Carlisle United v Morecambe

27/10/2020 19:45 Crawley Town v Tranmere Rovers

27/10/2020 19:45 Forest Green Rovers v Grimsby Town

27/10/2020 19:45 Harrogate Town v Stevenage

27/10/2020 19:45 Leyton Orient v Exeter City

27/10/2020 19:45 Mansfield Town v Barrow

27/10/2020 19:45 Newport County v Colchester United

27/10/2020 19:45 Port Vale v Cheltenham Town

27/10/2020 19:45 Scunthorpe United v Salford City

27/10/2020 19:45 Southend United v Oldham Athletic

27/10/2020 19:45 Walsall v Cambridge United

31/10/2020 15:00 Barrow v Bradford City

31/10/2020 15:00 Cheltenham Town v Forest Green Rovers

31/10/2020 15:00 Crawley Town v Cambridge United

31/10/2020 15:00 Exeter City v Carlisle United

31/10/2020 15:00 Leyton Orient v Bolton Wanderers

31/10/2020 15:00 Mansfield Town v Walsall

31/10/2020 15:00 Newport County v Harrogate Town

31/10/2020 15:00 Salford City v Oldham Athletic

31/10/2020 15:00 Scunthorpe United v Colchester United

31/10/2020 15:00 Southend United v Port Vale

31/10/2020 15:00 Stevenage v Grimsby Town

31/10/2020 15:00 Tranmere Rovers v Morecambe

November:

03/11/2020 20:00 Bolton Wanderers v Mansfield Town

03/11/2020 19:45 Bradford City v Southend United

03/11/2020 19:45 Cambridge United v Salford City

03/11/2020 19:45 Carlisle United v Newport County

03/11/2020 19:45 Colchester United v Stevenage

03/11/2020 19:45 Forest Green Rovers v Leyton Orient

03/11/2020 19:45 Grimsby Town v Barrow

03/11/2020 19:45 Harrogate Town v Tranmere Rovers

03/11/2020 19:45 Morecambe v Exeter City

03/11/2020 19:45 Oldham Athletic v Cheltenham Town

03/11/2020 19:45 Port Vale v Scunthorpe United

03/11/2020 19:45 Walsall v Crawley Town

14/11/2020 15:00 Bolton Wanderers v Salford City

14/11/2020 15:00 Bradford City v Exeter City

14/11/2020 15:00 Cambridge United v Barrow

14/11/2020 15:00 Carlisle United v Cheltenham Town

14/11/2020 15:00 Colchester United v Leyton Orient

14/11/2020 15:00 Forest Green Rovers v Mansfield Town

14/11/2020 15:00 Grimsby Town v Newport County

14/11/2020 15:00 Harrogate Town v Crawley Town

14/11/2020 15:00 Morecambe v Stevenage

14/11/2020 15:00 Oldham Athletic v Scunthorpe United

14/11/2020 15:00 Port Vale v Tranmere Rovers

14/11/2020 15:00 Walsall v Southend United

21/11/2020 15:00 Barrow v Forest Green Rovers

21/11/2020 15:00 Cheltenham Town v Walsall

21/11/2020 15:00 Crawley Town v Carlisle United

21/11/2020 15:00 Exeter City v Oldham Athletic

21/11/2020 15:00 Leyton Orient v Harrogate Town

21/11/2020 15:00 Mansfield Town v Colchester United

21/11/2020 15:00 Newport County v Port Vale

21/11/2020 15:00 Salford City v Bradford City

21/11/2020 15:00 Scunthorpe United v Morecambe

21/11/2020 15:00 Southend United v Cambridge United

21/11/2020 15:00 Stevenage v Bolton Wanderers

21/11/2020 15:00 Tranmere Rovers v Grimsby Town

24/11/2020 19:45 Barrow v Oldham Athletic

24/11/2020 19:45 Cheltenham Town v Cambridge United

24/11/2020 19:45 Crawley Town v Grimsby Town

24/11/2020 19:45 Exeter City v Colchester United

24/11/2020 19:45 Leyton Orient v Bradford City

24/11/2020 19:45 Mansfield Town v Harrogate Town

24/11/2020 19:45 Newport County v Walsall

24/11/2020 19:45 Salford City v Morecambe

24/11/2020 19:45 Scunthorpe United v Bolton Wanderers

24/11/2020 19:45 Southend United v Forest Green Rovers

24/11/2020 19:45 Stevenage v Port Vale

24/11/2020 19:45 Tranmere Rovers v Carlisle United

EFL fixtures

EFL fixtures 2020/21 in full (Image: GETTY)
December:

01/12/2020 20:00 Bolton Wanderers v Southend United

01/12/2020 19:45 Bradford City v Cheltenham Town

01/12/2020 19:45 Cambridge United v Mansfield Town

01/12/2020 19:45 Carlisle United v Salford City

01/12/2020 19:45 Colchester United v Crawley Town

01/12/2020 19:45 Forest Green Rovers v Newport County

01/12/2020 19:45 Grimsby Town v Exeter City

01/12/2020 19:45 Harrogate Town v Scunthorpe United

01/12/2020 19:45 Morecambe v Barrow

01/12/2020 19:45 Oldham Athletic v Tranmere Rovers

01/12/2020 19:45 Port Vale v Leyton Orient

01/12/2020 19:45 Walsall v Stevenage

05/12/2020 15:00 Barrow v Salford City

05/12/2020 15:00 Bolton Wanderers v Port Vale

05/12/2020 15:00 Bradford City v Carlisle United

05/12/2020 15:00 Cambridge United v Oldham Athletic

05/12/2020 15:00 Cheltenham Town v Exeter City

05/12/2020 15:00 Colchester United v Grimsby Town

05/12/2020 15:00 Harrogate Town v Forest Green Rovers

05/12/2020 15:00 Mansfield Town v Crawley Town

05/12/2020 15:00 Newport County v Morecambe

05/12/2020 15:00 Scunthorpe United v Leyton Orient

05/12/2020 15:00 Stevenage v Southend United

05/12/2020 15:00 Tranmere Rovers v Walsall

12/12/2020 15:00 Carlisle United v Stevenage

12/12/2020 15:00 Crawley Town v Barrow

12/12/2020 15:00 Exeter City v Tranmere Rovers

12/12/2020 15:00 Forest Green Rovers v Cambridge United

12/12/2020 15:00 Grimsby Town v Mansfield Town

12/12/2020 15:00 Leyton Orient v Newport County

12/12/2020 15:00 Morecambe v Harrogate Town

12/12/2020 15:00 Oldham Athletic v Bradford City

12/12/2020 15:00 Port Vale v Colchester United

12/12/2020 15:00 Salford City v Cheltenham Town

12/12/2020 15:00 Southend United v Scunthorpe United

12/12/2020 15:00 Walsall v Bolton Wanderers

15/12/2020 19:45 Cambridge United v Colchester United

15/12/2020 19:45 Carlisle United v Mansfield Town

15/12/2020 19:45 Cheltenham Town v Bolton Wanderers

15/12/2020 19:45 Crawley Town v Bradford City

15/12/2020 19:45 Exeter City v Harrogate Town

15/12/2020 19:45 Morecambe v Leyton Orient

15/12/2020 19:45 Oldham Athletic v Walsall

15/12/2020 19:45 Port Vale v Forest Green Rovers

15/12/2020 19:45 Salford City v Newport County

15/12/2020 19:45 Scunthorpe United v Barrow

15/12/2020 19:45 Southend United v Grimsby Town

15/12/2020 19:45 Tranmere Rovers v Stevenage

19/12/2020 15:00 Barrow v Cheltenham Town

19/12/2020 15:00 Bolton Wanderers v Tranmere Rovers

19/12/2020 15:00 Bradford City v Cambridge United

19/12/2020 15:00 Colchester United v Morecambe

19/12/2020 15:00 Forest Green Rovers v Carlisle United

19/12/2020 15:00 Grimsby Town v Scunthorpe United

19/12/2020 15:00 Harrogate Town v Salford City

19/12/2020 15:00 Leyton Orient v Crawley Town

19/12/2020 15:00 Mansfield Town v Southend United

19/12/2020 15:00 Newport County v Oldham Athletic

19/12/2020 15:00 Stevenage v Exeter City

19/12/2020 15:00 Walsall v Port Vale

26/12/2020 15:00 Cambridge United v Leyton Orient

26/12/2020 15:00 Carlisle United v Bolton Wanderers

26/12/2020 15:00 Cheltenham Town v Stevenage

26/12/2020 15:00 Crawley Town v Newport County

26/12/2020 15:00 Exeter City v Forest Green Rovers

26/12/2020 15:00 Morecambe v Grimsby Town

26/12/2020 15:00 Oldham Athletic v Harrogate Town

26/12/2020 15:00 Port Vale v Barrow

26/12/2020 15:00 Salford City v Walsall

26/12/2020 15:00 Scunthorpe United v Mansfield Town

26/12/2020 15:00 Southend United v Colchester United

26/12/2020 15:00 Tranmere Rovers v Bradford City

29/12/2020 19:45 Barrow v Tranmere Rovers

29/12/2020 20:00 Bolton Wanderers v Morecambe

29/12/2020 19:45 Bradford City v Port Vale

29/12/2020 19:45 Colchester United v Cheltenham Town

29/12/2020 19:45 Forest Green Rovers v Crawley Town

29/12/2020 19:45 Grimsby Town v Oldham Athletic

29/12/2020 19:45 Harrogate Town v Carlisle United

29/12/2020 19:45 Leyton Orient v Southend United

29/12/2020 19:45 Mansfield Town v Salford City

29/12/2020 19:45 Newport County v Exeter City

29/12/2020 19:45 Stevenage v Cambridge United

29/12/2020 19:45 Walsall v Scunthorpe United

January:

02/01/2021 15:00 Barrow v Exeter City

02/01/2021 15:00 Bolton Wanderers v Crawley Town

02/01/2021 15:00 Bradford City v Morecambe

02/01/2021 15:00 Colchester United v Tranmere Rovers

02/01/2021 15:00 Forest Green Rovers v Oldham Athletic

02/01/2021 15:00 Grimsby Town v Cambridge United

02/01/2021 15:00 Harrogate Town v Cheltenham Town

02/01/2021 15:00 Leyton Orient v Salford City

02/01/2021 15:00 Mansfield Town v Port Vale

02/01/2021 15:00 Newport County v Southend United

02/01/2021 15:00 Stevenage v Scunthorpe United

02/01/2021 15:00 Walsall v Carlisle United

09/01/2021 15:00 Cambridge United v Harrogate Town

09/01/2021 15:00 Carlisle United v Leyton Orient

09/01/2021 15:00 Cheltenham Town v Newport County

09/01/2021 15:00 Crawley Town v Stevenage

09/01/2021 15:00 Exeter City v Bolton Wanderers

09/01/2021 15:00 Morecambe v Walsall

09/01/2021 15:00 Oldham Athletic v Mansfield Town

09/01/2021 15:00 Port Vale v Grimsby Town

09/01/2021 15:00 Salford City v Colchester United

09/01/2021 15:00 Scunthorpe United v Bradford City

09/01/2021 15:00 Southend United v Barrow

09/01/2021 15:00 Tranmere Rovers v Forest Green Rovers

16/01/2021 15:00 Barrow v Scunthorpe United

16/01/2021 15:00 Bolton Wanderers v Cheltenham Town

16/01/2021 15:00 Bradford City v Crawley Town

16/01/2021 15:00 Colchester United v Cambridge United

16/01/2021 15:00 Forest Green Rovers v Port Vale

16/01/2021 15:00 Grimsby Town v Southend United

16/01/2021 15:00 Harrogate Town v Exeter City

16/01/2021 15:00 Leyton Orient v Morecambe

16/01/2021 15:00 Mansfield Town v Carlisle United

16/01/2021 15:00 Newport County v Salford City

16/01/2021 15:00 Stevenage v Tranmere Rovers

16/01/2021 15:00 Walsall v Oldham Athletic

23/01/2021 15:00 Cambridge United v Bradford City

23/01/2021 15:00 Carlisle United v Forest Green Rovers

23/01/2021 15:00 Cheltenham Town v Barrow

23/01/2021 15:00 Crawley Town v Leyton Orient

23/01/2021 15:00 Exeter City v Stevenage

23/01/2021 15:00 Morecambe v Colchester United

23/01/2021 15:00 Oldham Athletic v Newport County

23/01/2021 15:00 Port Vale v Walsall

23/01/2021 15:00 Salford City v Harrogate Town

23/01/2021 15:00 Scunthorpe United v Grimsby Town

23/01/2021 15:00 Southend United v Mansfield Town

23/01/2021 15:00 Tranmere Rovers v Bolton Wanderers

26/01/2021 19:45 Barrow v Grimsby Town

26/01/2021 19:45 Cheltenham Town v Oldham Athletic

26/01/2021 19:45 Crawley Town v Walsall

26/01/2021 19:45 Exeter City v Morecambe

26/01/2021 19:45 Leyton Orient v Forest Green Rovers

26/01/2021 19:45 Mansfield Town v Bolton Wanderers

26/01/2021 19:45 Newport County v Carlisle United

26/01/2021 19:45 Salford City v Cambridge United

26/01/2021 19:45 Scunthorpe United v Port Vale

26/01/2021 19:45 Southend United v Bradford City

26/01/2021 19:45 Stevenage v Colchester United

26/01/2021 19:45 Tranmere Rovers v Harrogate Town

30/01/2021 15:00 Bolton Wanderers v Leyton Orient

30/01/2021 15:00 Bradford City v Barrow

30/01/2021 15:00 Cambridge United v Crawley Town

30/01/2021 15:00 Carlisle United v Exeter City

30/01/2021 15:00 Colchester United v Scunthorpe United

30/01/2021 15:00 Forest Green Rovers v Cheltenham Town

30/01/2021 15:00 Grimsby Town v Stevenage

30/01/2021 15:00 Harrogate Town v Newport County

30/01/2021 15:00 Morecambe v Tranmere Rovers

30/01/2021 15:00 Oldham Athletic v Salford City

30/01/2021 15:00 Port Vale v Southend United

30/01/2021 15:00 Walsall v Mansfield Town

February:

06/02/2021 15:00 Barrow v Cambridge United

06/02/2021 15:00 Cheltenham Town v Carlisle United

06/02/2021 15:00 Crawley Town v Harrogate Town

06/02/2021 15:00 Exeter City v Bradford City

06/02/2021 15:00 Leyton Orient v Colchester United

06/02/2021 15:00 Mansfield Town v Forest Green Rovers

06/02/2021 15:00 Newport County v Grimsby Town

06/02/2021 15:00 Salford City v Bolton Wanderers

06/02/2021 15:00 Scunthorpe United v Oldham Athletic

06/02/2021 15:00 Southend United v Walsall

06/02/2021 15:00 Stevenage v Morecambe

06/02/2021 15:00 Tranmere Rovers v Port Vale

13/02/2021 15:00 Bolton Wanderers v Stevenage

13/02/2021 15:00 Bradford City v Salford City

13/02/2021 15:00 Cambridge United v Southend United

13/02/2021 15:00 Carlisle United v Crawley Town

13/02/2021 15:00 Colchester United v Mansfield Town

13/02/2021 15:00 Forest Green Rovers v Barrow

13/02/2021 15:00 Grimsby Town v Tranmere Rovers

13/02/2021 15:00 Harrogate Town v Leyton Orient

13/02/2021 15:00 Morecambe v Scunthorpe United

13/02/2021 15:00 Oldham Athletic v Exeter City

13/02/2021 15:00 Port Vale v Newport County

13/02/2021 15:00 Walsall v Cheltenham Town

20/02/2021 15:00 Barrow v Morecambe

20/02/2021 15:00 Cheltenham Town v Bradford City

20/02/2021 15:00 Crawley Town v Colchester United

20/02/2021 15:00 Exeter City v Grimsby Town

20/02/2021 15:00 Leyton Orient v Port Vale

20/02/2021 15:00 Mansfield Town v Cambridge United

20/02/2021 15:00 Newport County v Forest Green Rovers

20/02/2021 15:00 Salford City v Carlisle United

20/02/2021 15:00 Scunthorpe United v Harrogate Town

20/02/2021 15:00 Southend United v Bolton Wanderers

20/02/2021 15:00 Stevenage v Walsall

20/02/2021 15:00 Tranmere Rovers v Oldham Athletic

23/02/2021 20:00 Bolton Wanderers v Scunthorpe United

23/02/2021 19:45 Bradford City v Leyton Orient

23/02/2021 19:45 Cambridge United v Cheltenham Town

23/02/2021 19:45 Carlisle United v Tranmere Rovers

23/02/2021 19:45 Colchester United v Exeter City

23/02/2021 19:45 Forest Green Rovers v Southend United

23/02/2021 19:45 Grimsby Town v Crawley Town

23/02/2021 19:45 Harrogate Town v Mansfield Town

23/02/2021 19:45 Morecambe v Salford City

23/02/2021 19:45 Oldham Athletic v Barrow

23/02/2021 19:45 Port Vale v Stevenage

23/02/2021 19:45 Walsall v Newport County

27/02/2021 15:00 Bolton Wanderers v Barrow

27/02/2021 15:00 Carlisle United v Oldham Athletic

27/02/2021 15:00 Crawley Town v Exeter City

27/02/2021 15:00 Forest Green Rovers v Colchester United

27/02/2021 15:00 Harrogate Town v Grimsby Town

27/02/2021 15:00 Leyton Orient v Tranmere Rovers

27/02/2021 15:00 Mansfield Town v Morecambe

27/02/2021 15:00 Newport County v Stevenage

27/02/2021 15:00 Port Vale v Cambridge United

27/02/2021 15:00 Scunthorpe United v Cheltenham Town

27/02/2021 15:00 Southend United v Salford City

27/02/2021 15:00 Walsall v Bradford City

Leeds United: Marcelo Bielsa celebrates promotion with players
March:

02/03/2021 19:45 Barrow v Harrogate Town

02/03/2021 19:45 Bradford City v Mansfield Town

02/03/2021 19:45 Cambridge United v Scunthorpe United

02/03/2021 19:45 Cheltenham Town v Southend United

02/03/2021 19:45 Colchester United v Carlisle United

02/03/2021 19:45 Exeter City v Walsall

02/03/2021 19:45 Grimsby Town v Leyton Orient

02/03/2021 19:45 Morecambe v Crawley Town

02/03/2021 19:45 Oldham Athletic v Bolton Wanderers

02/03/2021 19:45 Salford City v Port Vale

02/03/2021 19:45 Stevenage v Forest Green Rovers

02/03/2021 19:45 Tranmere Rovers v Newport County

06/03/2021 15:00 Barrow v Mansfield Town

06/03/2021 15:00 Bradford City v Bolton Wanderers

06/03/2021 15:00 Cambridge United v Walsall

06/03/2021 15:00 Cheltenham Town v Port Vale

06/03/2021 15:00 Colchester United v Newport County

06/03/2021 15:00 Exeter City v Leyton Orient

06/03/2021 15:00 Grimsby Town v Forest Green Rovers

06/03/2021 15:00 Morecambe v Carlisle United

06/03/2021 15:00 Oldham Athletic v Southend United

06/03/2021 15:00 Salford City v Scunthorpe United

06/03/2021 15:00 Stevenage v Harrogate Town

06/03/2021 15:00 Tranmere Rovers v Crawley Town

09/03/2021 20:00 Bolton Wanderers v Cambridge United

09/03/2021 19:45 Carlisle United v Grimsby Town

09/03/2021 19:45 Crawley Town v Salford City

09/03/2021 19:45 Forest Green Rovers v Morecambe

09/03/2021 19:45 Harrogate Town v Colchester United

09/03/2021 19:45 Leyton Orient v Stevenage

09/03/2021 19:45 Mansfield Town v Cheltenham Town

09/03/2021 19:45 Newport County v Bradford City

09/03/2021 19:45 Port Vale v Oldham Athletic

09/03/2021 19:45 Scunthorpe United v Exeter City

09/03/2021 19:45 Southend United v Tranmere Rovers

09/03/2021 19:45 Walsall v Barrow

13/03/2021 15:00 Carlisle United v Bradford City

13/03/2021 15:00 Crawley Town v Mansfield Town

13/03/2021 15:00 Exeter City v Cheltenham Town

13/03/2021 15:00 Forest Green Rovers v Harrogate Town

13/03/2021 15:00 Grimsby Town v Colchester United

13/03/2021 15:00 Leyton Orient v Scunthorpe United

13/03/2021 15:00 Morecambe v Newport County

13/03/2021 15:00 Oldham Athletic v Cambridge United

13/03/2021 15:00 Port Vale v Bolton Wanderers

13/03/2021 15:00 Salford City v Barrow

13/03/2021 15:00 Southend United v Stevenage

13/03/2021 15:00 Walsall v Tranmere Rovers

20/03/2021 15:00 Barrow v Crawley Town

20/03/2021 15:00 Bolton Wanderers v Walsall

20/03/2021 15:00 Bradford City v Oldham Athletic

20/03/2021 15:00 Cambridge United v Forest Green Rovers

20/03/2021 15:00 Cheltenham Town v Salford City

20/03/2021 15:00 Colchester United v Port Vale

20/03/2021 15:00 Harrogate Town v Morecambe

20/03/2021 15:00 Mansfield Town v Grimsby Town

20/03/2021 15:00 Newport County v Leyton Orient

20/03/2021 15:00 Scunthorpe United v Southend United

20/03/2021 15:00 Stevenage v Carlisle United

20/03/2021 15:00 Tranmere Rovers v Exeter City

27/03/2021 15:00 Carlisle United v Cambridge United

27/03/2021 15:00 Colchester United v Bradford City

27/03/2021 15:00 Crawley Town v Port Vale

27/03/2021 15:00 Exeter City v Salford City

27/03/2021 15:00 Forest Green Rovers v Bolton Wanderers

27/03/2021 15:00 Grimsby Town v Walsall

27/03/2021 15:00 Harrogate Town v Southend United

27/03/2021 15:00 Leyton Orient v Oldham Athletic

27/03/2021 15:00 Morecambe v Cheltenham Town

27/03/2021 15:00 Newport County v Scunthorpe United

27/03/2021 15:00 Stevenage v Barrow

27/03/2021 15:00 Tranmere Rovers v Mansfield Town

April:

02/04/2021 15:00 Barrow v Newport County

02/04/2021 15:00 Bolton Wanderers v Colchester United

02/04/2021 15:00 Bradford City v Forest Green Rovers

02/04/2021 15:00 Cambridge United v Morecambe

02/04/2021 15:00 Cheltenham Town v Tranmere Rovers

02/04/2021 15:00 Mansfield Town v Leyton Orient

02/04/2021 15:00 Oldham Athletic v Stevenage

02/04/2021 15:00 Port Vale v Exeter City

02/04/2021 15:00 Salford City v Grimsby Town

02/04/2021 15:00 Scunthorpe United v Crawley Town

02/04/2021 15:00 Southend United v Carlisle United

02/04/2021 15:00 Walsall v Harrogate Town

05/04/2021 15:00 Carlisle United v Scunthorpe United

05/04/2021 15:00 Colchester United v Barrow

05/04/2021 15:00 Crawley Town v Oldham Athletic

05/04/2021 15:00 Exeter City v Mansfield Town

05/04/2021 15:00 Forest Green Rovers v Salford City

05/04/2021 15:00 Grimsby Town v Cheltenham Town

05/04/2021 15:00 Harrogate Town v Port Vale

05/04/2021 15:00 Leyton Orient v Walsall

05/04/2021 15:00 Morecambe v Southend United

05/04/2021 15:00 Newport County v Bolton Wanderers

05/04/2021 15:00 Stevenage v Bradford City

05/04/2021 15:00 Tranmere Rovers v Cambridge United

10/04/2021 15:00 Barrow v Carlisle United

10/04/2021 15:00 Bolton Wanderers v Harrogate Town

10/04/2021 15:00 Bradford City v Grimsby Town

10/04/2021 15:00 Cambridge United v Exeter City

10/04/2021 15:00 Cheltenham Town v Leyton Orient

10/04/2021 15:00 Mansfield Town v Newport County

10/04/2021 15:00 Oldham Athletic v Colchester United

10/04/2021 15:00 Port Vale v Morecambe

10/04/2021 15:00 Salford City v Stevenage

10/04/2021 15:00 Scunthorpe United v Tranmere Rovers

10/04/2021 15:00 Southend United v Crawley Town

10/04/2021 15:00 Walsall v Forest Green Rovers

17/04/2021 15:00 Carlisle United v Port Vale

17/04/2021 15:00 Colchester United v Walsall

17/04/2021 15:00 Crawley Town v Cheltenham Town

17/04/2021 15:00 Exeter City v Southend United

17/04/2021 15:00 Forest Green Rovers v Scunthorpe United

17/04/2021 15:00 Grimsby Town v Bolton Wanderers

17/04/2021 15:00 Harrogate Town v Bradford City

17/04/2021 15:00 Leyton Orient v Barrow

17/04/2021 15:00 Morecambe v Oldham Athletic

17/04/2021 15:00 Newport County v Cambridge United

17/04/2021 15:00 Stevenage v Mansfield Town

17/04/2021 15:00 Tranmere Rovers v Salford City

20/04/2021 19:45 Barrow v Port Vale

20/04/2021 20:00 Bolton Wanderers v Carlisle United

20/04/2021 19:45 Bradford City v Tranmere Rovers

20/04/2021 19:45 Colchester United v Southend United

20/04/2021 19:45 Forest Green Rovers v Exeter City

20/04/2021 19:45 Grimsby Town v Morecambe

20/04/2021 19:45 Harrogate Town v Oldham Athletic

20/04/2021 19:45 Leyton Orient v Cambridge United

20/04/2021 19:45 Mansfield Town v Scunthorpe United

20/04/2021 19:45 Newport County v Crawley Town

20/04/2021 19:45 Stevenage v Cheltenham Town

20/04/2021 19:45 Walsall v Salford City

24/04/2021 15:00 Cambridge United v Stevenage

24/04/2021 15:00 Carlisle United v Harrogate Town

24/04/2021 15:00 Cheltenham Town v Colchester United

24/04/2021 15:00 Crawley Town v Forest Green Rovers

24/04/2021 15:00 Exeter City v Newport County

24/04/2021 15:00 Morecambe v Bolton Wanderers

24/04/2021 15:00 Oldham Athletic v Grimsby Town

24/04/2021 15:00 Port Vale v Bradford City

24/04/2021 15:00 Salford City v Mansfield Town

24/04/2021 15:00 Scunthorpe United v Walsall

24/04/2021 15:00 Southend United v Leyton Orient

24/04/2021 15:00 Tranmere Rovers v Barrow

May:

01/05/2021 15:00 Barrow v Southend United

01/05/2021 15:00 Bolton Wanderers v Exeter City

01/05/2021 15:00 Bradford City v Scunthorpe United

01/05/2021 15:00 Colchester United v Salford City

01/05/2021 15:00 Forest Green Rovers v Tranmere Rovers

01/05/2021 15:00 Grimsby Town v Port Vale

01/05/2021 15:00 Harrogate Town v Cambridge United

01/05/2021 15:00 Leyton Orient v Carlisle United

01/05/2021 15:00 Mansfield Town v Oldham Athletic

01/05/2021 15:00 Newport County v Cheltenham Town

01/05/2021 15:00 Stevenage v Crawley Town

01/05/2021 15:00 Walsall v Morecambe

08/05/2021 15:00 Cambridge United v Grimsby Town

08/05/2021 15:00 Carlisle United v Walsall

08/05/2021 15:00 Cheltenham Town v Harrogate Town

08/05/2021 15:00 Crawley Town v Bolton Wanderers

08/05/2021 15:00 Exeter City v Barrow

08/05/2021 15:00 Morecambe v Bradford City

08/05/2021 15:00 Oldham Athletic v Forest Green Rovers

08/05/2021 15:00 Port Vale v Mansfield Town

08/05/2021 15:00 Salford City v Leyton Orient

08/05/2021 15:00 Scunthorpe United v Stevenage

08/05/2021 15:00 Southend United v Newport County

08/05/2021 15:00 Tranmere Rovers v Colchester United
"""

def convert_date(date_string) :
    splitted = date_string.split('/')
    mo = get_number_month(int(splitted[1])-1)
    da = int(splitted[0])
    return mo+' '+str(da)

import re

correct_team_names = {
    'Arsenal':'Arsenal',
    'Aston Villa':'Aston Villa',
    'Brighton':'Brighton & Hove Albion',
    'Burnley':'Burnley',
    'Chelsea':'Chelsea',
    'Crystal Palace':'Crystal Palace',
    'Everton':'Everton',
    'Fulham':'Fulham', 
    'Leeds':'Leeds United',
    'Leed':'Leeds United',
    'Leicester':'Leicester City', 
    'Liverpool':'Liverpool', 
    'Man Utd':'Manchester United',
    'Man City':'Manchester City',
    'Newcastle':'Newcastle United', 
    'Sheffield Utd':'Sheffield United',
    'Sheff Utd':'Sheffield United',
    'Sheffield United':'Sheffield United',
    'Southampton':'Southampton',
    'Spurs':'Tottenham Hotspur',
    'West Brom':'West Bromwich Albion', 
    'West Ham':'West Ham United',
    'Wolves':'Wolverhampton Wanderers',
    'A.F.C. Bournemouth':'AFC Bournemouth',
    'Barnsley':'Barnsley',
    'Birmingham City':'Birmingham City',
    'Blackburn Rovers':'Blackburn Rovers',
    'Brentford':'Brentford',
    'Bristol City':'Bristol City',
    'Cardiff City':'Cardiff City',
    'Coventry City':'Coventry City',
    'Derby County':'Derby County',
    'Huddersfield Town':'Huddersfield Town',
    'Luton Town':'Luton Town',
    'Middlesbrough':'Middlesbrough',
    'Millwall':'Millwall',
    'Norwich City':'Norwich City',
    'Nottingham Forest':'Nottingham Forest',
    'Preston North End':'Preston North End',
    'Queens Park Rangers':'Queens Park Rangers',
    'Reading':'Reading',
    'Rotherham United':'Rotherham United',
    'Sheffield Wednesday':'Sheffield Wednesday',
    'Stoke City':'Stoke City',
    'Swansea City':'Swansea City',
    'Watford':'Watford',
    'Wycombe Wanderers':'Wycombe Wanderers',
}

lower_conversions = {
    'A.F.C. Wimbledon':'AFC Wimbledon',
}

special_cases = {
    'May 13' :[['Aston Villa', 'Everton']],
    'January 23':[['Aston Villa', 'Newcastle United']],
    'February 17':[['Burnley', 'Fulham']],
    'December 28':[['Everton', 'Manchester City']],
    'March 21':[['Aston Villa', 'Tottenham Hotspur']],
    'May 2':[['Manchester United', 'Liverpool']]
}

months_shortened_dict = {
    'Feb.':'February',
    'Jan.':'January',
    'Dec.':'December',
    'Nov.':'November',
    'Oct.':'October',
    'Sept.':'September',
}

def get_schedule_prem() :
    schedule_dict = {}
    for line in schedule_prem.split('\n\n') :
        lines = [lin for lin in line.split('\n') if lin != '']
        date_array = [split_piece for split_piece in lines[0].split(' ') if split_piece != '']
        date = ' '.join([date_array[-1], date_array[-2]])
        if date in special_cases :
            dont_add = special_cases[date]
        else :
            dont_add = []
        games = []
        for lin in lines[1:] :
            lin = lin.split('(')[0]
            lin = ' '.join(lin.split(' ')[1:])[:-1]
            game = lin.split(' v ')
            if game != [''] :
                game = [correct_team_names[game[0]], correct_team_names[game[1]]]
                if not game in dont_add :
                    games.append(game)
        schedule_dict[date] = games
    schedule_dict['February 22'].append(['Brighton & Hove Albion', 'Crystal Palace'])
    return schedule_dict

def get_schedule_championship() :
    schedule_dict = {}
    for line in schedule_championship.split('\n\n') :
        lines = [lin for lin in line.split('\n') if lin != '']
        date = lines[0].split(',')[1][1:]
        month = date.split(' ')[0]
        if month in months_shortened_dict :
            month = months_shortened_dict[month]
            date = ' '.join([month, date.split(' ')[1]])
        games = []
        for lin in lines[1:] :
            game = lin.split(' v ')
            if game != [''] :
                game = [correct_team_names[game[0]], correct_team_names[game[1]]]
                games.append(game)
        schedule_dict[date] = games
    return schedule_dict

def get_schedule_league_one() :
    schedule_dict = {}
    for finding in re.findall('[0-9]+/[0-9]+/[0-9]+ [^\n]+', schedule_leagueone) :
        finding_space_split = finding.split(' ')
        sd_key = convert_date(finding_space_split[0])
        finding = ' '.join(finding_space_split[2:])
        teams_involved = finding.split(' v ')
        for team_i_ind, team_i in enumerate(teams_involved) :
            if team_i in lower_conversions :
                teams_involved[team_i_ind] = lower_conversions[team_i]
        if sd_key in schedule_dict :
            schedule_dict[sd_key].append(teams_involved)
        else :
            schedule_dict[sd_key] = [teams_involved]
    return schedule_dict

def get_schedule_league_two() :
    schedule_dict = {}
    for finding in re.findall('[0-9]+/[0-9]+/[0-9]+ [^\n]+', schedule_leaguetwo) :
        finding_space_split = finding.split(' ')
        sd_key = convert_date(finding_space_split[0])
        finding = ' '.join(finding_space_split[2:])
        teams_involved = finding.split(' v ')
        for team_i_ind, team_i in enumerate(teams_involved) :
            if team_i in lower_conversions :
                teams_involved[team_i+ind] = lower_conversions[team_i]
        if sd_key in schedule_dict :
            schedule_dict[sd_key].append(teams_involved)
        else :
            schedule_dict[sd_key] = [teams_involved]
    return schedule_dict

def team_in_gameday(team, gameday) :
    for game in gameday :
        if team in game :
            if team == game[0] :
                return True, game[1], get_stadium(game[0]), 0
            return True, game[0], get_stadium(game[0]), 1
    return False, '', None

def get_games_in_a_month(month, schedule, team) :
    games = {}
    for date in schedule :
        m = date.split(' ')[0]
        tig = team_in_gameday(team, schedule[date])
        if month == m and tig[0] :
            games[date] = [tig[1], tig[2], tig[3]]
    return games
    
def replace_old_teams_in_schedule(schedule, new_teams, teams_in_league) :
    old_teams = []
    for date in schedule :
        for game in schedule[date] :
            for team in game :
                if (not team in teams_in_league) and (not team in old_teams) :
                    old_teams.append(team)
    print(old_teams)
    new_schedule = {}
    for date in schedule :
        new_schedule[date] = []
        for game in schedule[date] :
            new_insertion = []
            for team in game :
                if team in old_teams :
                    new_insertion.append(new_teams[old_teams.index(team)])
                else :
                    new_insertion.append(team)
            new_schedule[date].append(new_insertion)
    return new_schedule

def scramble_schedule(schedule) :
    dates = list(schedule.keys())
    random.shuffle(dates)
    values = [schedule[date] for date in dates]
    random.shuffle(values)
    return {dates[i]:values[i] for i in range(len(values))}


"""
c = 0
schedule = get_schedule()
amount_of_games = {correct_team_names[t]:0 for t in correct_team_names}
villa_games = []
for date in schedule :
    games_on_date = schedule[date]
    for game in games_on_date :
        t1, t2 = game
        amount_of_games[t1] += 1
        amount_of_games[t2] += 1
        
        if t1 == 'Aston Villa' or t2 == 'Aston Villa' :
            if game in villa_games :
                print(game)
                print('ITS A REPEAT _________________________________________________________________________________________________________')
                print()
                print()
                print()
            else :
                villa_games.append(game)
        

for element in amount_of_games :
    print(element, amount_of_games[element])
"""

"""
schedule = get_schedule_championship()
print()
print()
print()
for date in schedule :
    print(date, schedule[date])
    print()
"""
