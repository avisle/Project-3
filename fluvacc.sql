create table fluvacc_all 
as select * from fluvacc19
union all
select * from fluvacc20
union all
select * from fluvacc21
union all
select * from fluvacc22
;

select * from fluvacc_all;

select flu_season, percentage_healthcare_professionals_vaccinated FROM fluvacc_all where county = 'Yolo';

drop table fluvacc_all;

