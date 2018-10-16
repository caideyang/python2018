-- 1、自行创建测试数据；
-- 建库脚本 school20181008.sql

--2、查询学生总人数；
select count(1) as "学生总数量" from student;
-- +------------+
-- | 学生总数量 |
-- +------------+
-- |        365 |
-- +------------+
-- 1 row in set
-- 3、查询“生物”课程和“物理”课程成绩都及格的学生id和姓名；
select sc.student_id as "编号",s.sname as "姓名"
from score sc, student s , course c
where c.cname in ("生物","物理")
and sc.course_id = c.cid
and sc.student_id = s.sid
and sc.score >= 60
group by sc.student_id having count(sc.student_id)=2;
-- +------+--------+
-- | 编号 | 姓名   |
-- +------+--------+
-- |  240 | 刘先承 |
-- |  241 | 彭 啟  |
-- |  242 | 袁 亮  |
-- |  243 | 贾天顺 |
-- |  244 | 何正良 |
-- ......
-- 101 rows in set
-- 4、查询每个年级的班级数，取出班级数最多的前三个年级；
select g.gid as "年级编号" , g.gname as "年级" ,count(c.grade_id) as "班级数量"
from class c ,class_grade g where c.grade_id = g.gid group by c.grade_id order by 3 desc  limit 3;
-- +----------+--------+----------+
-- | 年级编号 | 年级   | 班级数量 |
-- +----------+--------+----------+
-- |        6 | 六年级 |        9 |
-- |        1 | 一年级 |        7 |
-- |        5 | 五年级 |        7 |
-- +----------+--------+----------+
-- 3 rows in set
-- 5、查询平均成绩最高和最低的学生的id和姓名以及平均成绩；
-- -- 平均成绩最高的学生：
-- select sc.student_id as "编号" ,s.sname as "姓名",  avg(sc.score) as "平均成绩"
-- from score sc , student s where s.sid = sc.student_id group by sc.student_id order by avg(sc.score) desc  limit 1;
-- -- +------+--------+----------+
-- -- | 编号 | 姓名   | 平均成绩 |
-- -- +------+--------+----------+
-- -- |  360 | 贺仕西 | 94.6667  |
-- -- +------+--------+----------+
-- -- 1 row in set
-- -- 平均成绩最低的学生：
-- select sc.student_id as "编号" ,s.sname as "姓名",  avg(sc.score) as "平均成绩"
-- from score sc , student s where s.sid = sc.student_id group by sc.student_id order by avg(sc.score) asc  limit 1;
-- -- +------+-------+----------+
-- -- | 编号 | 姓名  | 平均成绩 |
-- -- +------+-------+----------+
-- -- |  308 | 林 强 | 39.3333  |
-- -- +------+-------+----------+
-- -- 1 row in set
select max.student_id as '平均分最高学生编号',max.sname as '学生姓名',max.avg_score as '平均分数',
min.student_id as '平均分最低学生编号',min.sname as '学生姓名',min.avg_score as '平均分数' from
(select sc.student_id as student_id ,s.sname ,  avg(sc.score) as avg_score
from score sc , student s where s.sid = sc.student_id group by sc.student_id order by avg(sc.score) desc  limit 1) max
,(select sc.student_id, s.sname,  avg(sc.score) as avg_score
from score sc , student s where s.sid = sc.student_id group by sc.student_id order by avg(sc.score) asc  limit 1) min ;
+--------------------+----------+----------+--------------------+----------+----------+
| 平均分最高学生编号 | 学生姓名 | 平均分数 | 平均分最低学生编号 | 学生姓名 | 平均分数 |
+--------------------+----------+----------+--------------------+----------+----------+
|                176 | 兰文军   | 93.0000  |                174 | 赵 明    | 39.3333  |
+--------------------+----------+----------+--------------------+----------+----------+
1 row in set
-- 6、查询每个年级的学生人数；
select g.gname as "年级" ,count(s.sid) as "人数"
from  student s , class c, class_grade g where s.class_id = c.cid and c.grade_id = g.gid group by g.gid;
-- +--------+------+
-- | 年级   | 人数 |
-- +--------+------+
-- | 一年级 |   58 |
-- | 二年级 |   44 |
-- | 三年级 |   35 |
-- | 四年级 |   30 |
-- | 五年级 |   70 |
-- | 六年级 |  128 |
-- +--------+------+
-- 6 rows in set
-- 7、查询每位学生的学号，姓名，选课数，平均成绩；
select sc.student_id as "编号" ,s.sname as "姓名", count(sc.score) as "选课数量", avg(sc.score) as "平均成绩"
from score sc , student s where s.sid = sc.student_id group by sc.student_id;
-- +------+----------+----------+----------+
-- | 编号 | 姓名     | 选课数量 | 平均成绩 |
-- +------+----------+----------+----------+
-- |    1 | 乔丹     |        5 | 79.2000  |
-- |    2 | 艾弗森   |        5 | 77.2000  |
-- |    3 | 科比     |        5 | 74.2000  |
-- ......
-- 365 rows in set
-- 8、查询学生编号为“2”的学生的姓名、该学生成绩最高的课程名、成绩最低的课程名及分数；
select min.sname as '姓名',min.cname as '最低分课程',min.score as '分数',max.cname as '最高分课程',max.score as '分数' from
(select sc.student_id,s.sname, sc.course_id, sc.score, c.cname from score sc ,student s , course c
where sc.student_id=2 and c.cid = sc.course_id  and s.sid = sc.student_id order by student_id ,score limit 1) min
,(select sc.student_id,s.sname, sc.course_id, sc.score, c.cname from score sc ,student s , course c
where sc.student_id=2 and c.cid = sc.course_id  and s.sid = sc.student_id order by student_id ,score desc limit 1 ) max ;
-- +--------+------------+------+------------+------+
-- | 姓名   | 最低分课程 | 分数 | 最高分课程 | 分数 |
-- +--------+------------+------+------------+------+
-- | 艾弗森 | 体育       |   30 | 数学       |  100 |
-- +--------+------------+------+------------+------+
-- 1 row in set
-- 9、查询姓“李”的老师的个数和所带班级数；
select count(distinct t.tname) as '李姓老师数量', count(tc.cid) as '班级数量' from teacher t , teacher2cls tc
where t.tid = tc.tid and t.tname like '李%';
-- +--------------+----------+
-- | 李姓老师数量 | 班级数量 |
-- +--------------+----------+
-- |            2 |        8 |
-- +--------------+----------+
-- 1 row in set
-- 10、查询班级数小于5的年级id和年级名；
select g.gid as "编号", g.gname as "年级"  from class_grade g, class c
where g.gid = c.grade_id group by grade_id having count(cid)<5;
-- +------+--------+
-- | 编号 | 年级   |
-- +------+--------+
-- |    4 | 四年级 |
-- +------+--------+
-- 1 row in set
-- 11、查询班级信息，包括班级id、班级名称、年级、年级级别(12为低年级，34为中年级，56为高年级)，示例结果如下；
select c.cid as '编号',c.caption as '班级', g.gname as '年级',
case
when g.gname in ('一年级','二年级') then '低年级'
when g.gname in ('三年级','四年级') then '中年级'
else '高年级'
end as '级别'
from class c left join class_grade g on c.grade_id = g.gid;
-- +------+----------+--------+--------+
-- | 编号 | 班级     | 年级   | 级别   |
-- +------+----------+--------+--------+
-- |    1 | 一年一班 | 一年级 | 低年级 |
-- |    2 | 二年一班 | 二年级 | 低年级 |
-- |    3 | 三年一班 | 三年级 | 中年级 |
-- |    4 | 四年一班 | 四年级 | 中年级 |
-- |    5 | 五年一班 | 五年级 | 高年级 |
-- |    6 | 六年一班 | 六年级 | 高年级 |
-- |    7 | 一年二班 | 一年级 | 低年级 |
-- |    8 | 一年三班 | 一年级 | 低年级 |
-- ......
-- 38 rows in set
-- 12、查询学过“张三”老师2门课以上的同学的学号、姓名；
select sid as '学号', sname as '姓名' from student s
inner join
(select sc.student_id  from score sc where sc.course_id in
(select cid from course where teacher_id =
(select tid from teacher where tname='张三') )
group by sc.student_id having count(sc.student_id)>=2 ) sc
on sc.student_id = s.sid  ;
-- +------+----------+
-- | 学号 | 姓名     |
-- +------+----------+
-- |    1 | 乔丹     |
-- |    2 | 艾弗森   |
-- |    3 | 科比     |
-- |    4 | 奥尼尔   |
-- ......
-- 309 rows in set

-- 13、查询教授课程超过2门的老师的id和姓名；
select t.tid as '编号',t.tname as '姓名', c.course_count as '课程数量' from teacher t
inner join
(select teacher_id , count(teacher_id) as course_count
from course group by teacher_id having count(teacher_id)>=2) c
on t.tid = c.teacher_id ;
-- +------+------+----------+
-- | 编号 | 姓名 | 课程数量 |
-- +------+------+----------+
-- |    2 | 张三 |        3 |
-- |    3 | 李四 |        3 |
-- +------+------+----------+
-- 2 rows in set
-- 14、查询学过编号“1”课程和编号“2”课程的同学的学号、姓名；
select sc.student_id as '编号',s.sname as '姓名' from score sc, student s
where sc.course_id in (1,2) and sc.student_id = s.sid
group by student_id having count(student_id)=2 ;
-- +------+----------+
-- | 编号 | 姓名     |
-- +------+----------+
-- |    1 | 乔丹     |
-- |    2 | 艾弗森   |
-- |    3 | 科比     |
-- ......
-- 288 rows in set
-- 15、查询没有带过高年级的老师id和姓名；
select tid as '编号', tname as '姓名' from teacher
where tid not in
(select tid from teacher2cls tc where cid in
(select t.cid from
(select c.cid ,c.caption, g.gname ,
case
when g.gname in ('一年级','二年级') then '低年级'
when g.gname in ('三年级','四年级') then '中年级'
else '高年级'  end as level
from class c, class_grade g
where c.grade_id = g.gid ) t
where  t.level="高年级"));
-- +------+------+
-- | 编号 | 姓名 |
-- +------+------+
-- |   11 | 远传 |
-- |   12 | egon |
-- +------+------+
-- 2 rows in set
-- 16、查询学过“张三”老师所教的所有课的同学的学号、姓名；
select distinct student_id as '编号', sname as '姓名'
from score sc , student s
where course_id in
(select cid from course
where teacher_id=(select tid
from teacher where tname='张三'))
and s.sid = sc.student_id ;
-- +------+----------+
-- | 编号 | 姓名     |
-- +------+----------+
-- |    1 | 乔丹     |
-- |    2 | 艾弗森   |
-- |    3 | 科比     |
-- |    4 | 奥尼尔   |
-- |    5 | 姚明     |
-- ......
-- 365 rows in set
-- 17、查询带过超过2个班级的老师的id和姓名；
select t.tid as '编号', t.tname as '姓名', t2c.count as '班级数'
from teacher t
inner join (select tid,count(tid) as count
from teacher2cls group by tid having count(tid)>2)  t2c
on t.tid = t2c.tid;
-- +------+------+--------+
-- | 编号 | 姓名 | 班级数 |
-- +------+------+--------+
-- |    1 | Alex |      3 |
-- |    2 | 张三 |      8 |
-- |    3 | 李四 |      6 |
-- |    4 | 王五 |      5 |
-- |    5 | 李一 |      3 |
-- |    6 | 里尔 |      3 |
-- |    8 | 周军 |      3 |
-- |    9 | 胜伟 |      3 |
-- +------+------+--------+
-- 8 rows in set
-- 18、查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；
select sid as '编号', sname as '姓名'
from student where sid in
(select sc2.student_id from
(select student_id,course_id,score from score where course_id = 2) sc2 ,
(select student_id,course_id,score from score where course_id = 1) sc1
where sc2.student_id = sc1.student_id
and sc2.score < sc1.score);
-- +------+----------+
-- | 编号 | 姓名     |
-- +------+----------+
-- |    7 | 斯科拉   |
-- |    8 | 詹姆斯   |
-- |    9 | 韦德     |
-- |   10 | 费舍尔   |
-- |   11 | 保罗     |
-- ......
-- 131 rows in set
-- 19、查询所带班级数最多的老师id和姓名；
select t.tid as '编号', t.tname as '姓名', t2c.count as '班级数'
from teacher t
inner join (select tid,count(tid) as count
from teacher2cls group by tid having count(tid)>2)  t2c
on t.tid = t2c.tid order by 3 desc limit 2;
-- +------+------+--------+
-- | 编号 | 姓名 | 班级数 |
-- +------+------+--------+
-- |    2 | 张三 |      8 |
-- |    3 | 李四 |      6 |
-- +------+------+--------+
-- 2 rows in set
-- 20、查询有课程成绩小于60分的同学的学号、姓名；
select distinct sc.student_id as '编号', s.sname as '姓名'
from score sc, student s where sc.score < 60 and s.sid = sc.student_id;
-- +------+----------+
-- | 编号 | 姓名     |
-- +------+----------+
-- |    2 | 艾弗森   |
-- |    3 | 科比     |
-- |    4 | 奥尼尔   |
-- |    5 | 姚明     |
-- ......
-- 232 rows in set
-- 21、查询没有学全所有课的同学的学号、姓名；
select sc.student_id as '编号', s.sname as '姓名'
from score sc, student s
where s.sid = sc.student_id group by student_id
having count(student_id) < (select count(1) from course)
order by 2 asc;
-- +------+----------+
-- | 编号 | 姓名     |
-- +------+----------+
-- |  348 | 丁大杰   |
-- |  161 | 丁家峰   |
-- |   72 | 丁海林   |
-- |  167 | 严建国   |
-- |   95 | 乔丹     |
-- |    1 | 乔丹     |
-- ......
-- 362 rows in set
-- 22、查询至少有一门课与学号为“1”的同学所学相同的同学的学号和姓名；
select distinct sc.student_id as '编号', s.sname as '姓名'
from score sc, student s
where sc.course_id in
(select course_id from score where student_id=1)
and sc.student_id = s.sid;
-- +------+----------+
-- | 编号 | 姓名     |
-- +------+----------+
-- |    1 | 乔丹     |
-- |    2 | 艾弗森   |
-- |    3 | 科比     |
-- |    4 | 奥尼尔   |
-- .....
-- 186 rows in set
-- 23、查询至少学过学号为“1”同学所选课程中任意一门课的其他同学学号和姓名；
select  sc.student_id as '编号', s.sname as '姓名'
from score sc, student s
where sc.course_id in
(select course_id from score where student_id=1)
and sc.student_id = s.sid
group by sc.student_id
having count(sc.student_id) =
(select count(1) from score where student_id=1 );
-- +------+----------+
-- | 编号 | 姓名     |
-- +------+----------+
-- |    1 | 乔丹     |
-- |    2 | 艾弗森   |
-- |    3 | 科比     |
-- |    4 | 奥尼尔   |
-- |    5 | 姚明     |
-- ......
-- 186 rows in set
-- 24、查询和“2”号同学学习的课程完全相同的其他同学的学号和姓名；
select sid as '编号',sname as '姓名'  from student
where sid in  (select student_id from score
group by student_id
having count(course_id) =
(select count(1) from score where student_id = 2))
and sid not in (select distinct student_id
from score where student_id in
(select student_id from score
group by student_id
having count(course_id) =
(select count(1) from score where student_id = 2))
and course_id not in
(select course_id from  score where student_id = 2));
-- +------+--------+
-- | 编号 | 姓名   |
-- +------+--------+
-- |    2 | 艾弗森 |
-- |    3 | 科比   |
-- |    4 | 奥尼尔 |
-- |    5 | 姚明   |
......
-- 23 rows in set
-- 25、删除学习“张三”老师课的score表记录；
delete from score where course_id in
(select cid from course where teacher_id in
(select tid from teacher where tname='张三'));
-- Query OK, 720 rows affected
-- 26、向score表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“2”课程的同学学号；②插入“2”号课程的平均成绩；
insert into score(student_id, course_id, score)
select s.sid, s.cid, av.avg_score
from (select sid, '2' as cid
from student where sid not in
(select student_id from score where course_id=2))  as s,
(select avg(score) as 'avg_score' from score where course_id = '2') as av;
-- Query OK, 11 rows affected
-- 27、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示：
-- 学生ID,语文,数学,英语,课程数和平均分；
select sc.student_id as '学生ID',
(select s.score from score s left join course c on s.course_id = c.cid
where c.cname = '语文' and s.student_id = sc.student_id) as '语文',
(select s.score from score s left join course c on s.course_id = c.cid
where c.cname = '数学' and s.student_id = sc.student_id) as '数学',
(select s.score from score s left join course c on s.course_id = c.cid
where c.cname = '英语' and s.student_id = sc.student_id) as '英语',
count(sc.course_id) as '选课数', avg(sc.score) as '平均分'
from score  sc  group by sc.student_id   order by avg(sc.score);
-- +----------+------+------+------+--------+---------+
-- | 学生ID   | 语文 | 数学 | 英语 | 选课数 | 平均分  |
-- +----------+------+------+------+--------+---------+
-- |      308 |   80 |   38 |   28 |      6 | 39.3333 |
-- |      349 |   28 |   80 |   59 |      6 | 41.8333 |
-- |      286 |   38 |   95 |   21 |      5 | 42.0000 |
-- |      284 |   67 |   28 |   40 |      5 | 42.2000 |
-- |      293 |   60 |   60 |   95 |      6 | 46.3333 |
-- |      122 |   67 |   67 |   38 |      5 | 46.4000 |
-- ......
-- 365 rows in set
-- 28、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
select sc.course_id as '课程ID',
(select max(s.score) from score s where s.course_id = sc.course_id ) as "最高分",
(select min(s.score) from score s where s.course_id = sc.course_id  ) as "最低分"
from  score sc  group by sc.course_id;
-- +--------+--------+--------+
-- | 课程ID | 最高分 | 最低分 |
-- +--------+--------+--------+
-- |      1 |    100 |     19 |
-- |      2 |     99 |     17 |
-- |      3 |     99 |     20 |
-- |      4 |     99 |     14 |
-- |      5 |    100 |     15 |
-- |      6 |    100 |     10 |
-- |      7 |    100 |     12 |
-- |      8 |    100 |     21 |
-- +--------+--------+--------+
-- 8 rows in set
-- 29、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
select c.cid as '编号', c.cname as '名称', s.avg_score as '平均分' , s .percent as '及格率'
from course c inner join
(select sc.course_id, avg(sc.score) as avg_score,
concat(
sum(case when sc.score >= 60 then 1 else 0 end) / count(sc.score) * 100 , '%')as percent
from score sc group by sc.course_id) as s
on c.cid = s.course_id
order by 3 asc, 4 desc;
-- +------+------+---------+----------+
-- | 编号 | 名称 | 平均分  | 及格率   |
-- +------+------+---------+----------+
-- |    2 | 数学 | 73.3178 | 78.6301% |
-- |    7 | 政治 | 73.7968 | 78.6096% |
-- |    1 | 语文 | 73.7987 | 78.8591% |
-- |    3 | 英语 | 74.1412 | 78.8136% |
-- |    4 | 生物 | 74.3462 | 79.1209% |
-- |    8 | 体育 | 74.5699 | 79.5699% |
-- |    6 | 化学 | 75.2368 | 80.2632% |
-- |    5 | 物理 | 75.4111 | 80.0000% |
-- +------+------+---------+----------+
-- 8 rows in set
-- 30、课程平均分从高到低显示（显示任课老师）；
select sc.course_id as '课程ID' , c.cname as '课程名称' , sc.avg_score as '平均分', t.tname as '教师'
from
teacher t ,
course c,
(select course_id,avg(score) as avg_score from score group by course_id) sc
where sc.course_id = c.cid and c.teacher_id = t.tid
order by sc.avg_score desc;
-- +--------+----------+---------+------+
-- | 课程ID | 课程名称 | 平均分  | 教师 |
-- +--------+----------+---------+------+
-- |      5 | 物理     | 75.4111 | 张三 |
-- |      6 | 化学     | 75.2368 | 李四 |
-- |      8 | 体育     | 74.5699 | 张三 |
-- |      4 | 生物     | 74.3462 | 王五 |
-- |      3 | 英语     | 74.1412 | 李四 |
-- |      1 | 语文     | 73.7987 | Alex |
-- |      7 | 政治     | 73.7968 | 李四 |
-- |      2 | 数学     | 73.3178 | 王五 |
-- +--------+----------+---------+------+
-- 8 rows in set
-- 31、查询各科成绩前三名的记录(不考虑成绩并列情况) ；
select c.cid as '编号', c.cname as '课程' ,
(select sc1.score from score sc1 where sc1.course_id = sc.course_id order by sc1.score desc limit 0,1) as '最高分',
(select sc1.score from score sc1 where sc1.course_id = sc.course_id order by sc1.score desc limit 1,1) as '第二高分',
(select sc1.score from score sc1 where sc1.course_id = sc.course_id order by sc1.score desc limit 2,1) as '第三高分'
from score sc , course c where c.cid = sc.course_id
group by sc.course_id;
-- +------+------+--------+----------+----------+
-- | 编号 | 课程 | 最高分 | 第二高分 | 第三高分 |
-- +------+------+--------+----------+----------+
-- |    1 | 语文 |     99 |       98 |       95 |
-- |    2 | 数学 |    100 |       98 |       95 |
-- |    3 | 英语 |    100 |       96 |       95 |
-- |    4 | 生物 |    100 |      100 |      100 |
-- |    5 | 物理 |    100 |      100 |      100 |
-- |    6 | 化学 |    100 |      100 |      100 |
-- |    7 | 政治 |    100 |      100 |      100 |
-- |    8 | 体育 |    100 |      100 |      100 |
-- +------+------+--------+----------+----------+
-- 8 rows in set
-- 32、查询每门课程被选修的学生数；
 select sc.course_id as '编号', c.cname as '名称', count(sc.course_id) as '人数'
 from score sc, course c where c.cid = sc.course_id group by course_id;
-- +------+------+------+
-- | 编号 | 名称 | 人数 |
-- +------+------+------+
-- |    1 | 语文 |  242 |
-- |    2 | 数学 |  291 |
-- |    3 | 英语 |  285 |
-- |    4 | 生物 |  182 |
-- |    5 | 物理 |  180 |
-- |    6 | 化学 |   76 |
-- |    7 | 政治 |  187 |
-- |    8 | 体育 |  186 |
-- +------+------+------+
-- 8 rows in set
-- 33、查询选修了2门以上课程的全部学生的学号和姓名；
select s.sid as '学号', s.sname as '姓名' from student s
where s.sid in (select student_id from score group by student_id having count(student_id)>=2);
-- +------+----------+
-- | 学号 | 姓名     |
-- +------+----------+
-- |    1 | 乔丹     |
-- |    2 | 艾弗森   |
-- |    3 | 科比     |
-- |    4 | 奥尼尔   |
-- |    5 | 姚明     |
-- 363 rows in set
-- 34、查询男生、女生的人数，按倒序排列；
select gender as '性别', count(gender) as '数量' from student group by gender;
-- +------+------+
-- | 性别 | 数量 |
-- +------+------+
-- | 女   |  160 |
-- | 男   |  206 |
-- +------+------+
-- 2 rows in set
-- 35、查询姓“张”的学生名单；
select * from student where sname like '张%';
-- +-----+--------+--------+----------+
-- | sid | sname  | gender | class_id |
-- +-----+--------+--------+----------+
-- |  18 | 张三   | 男     |        1 |
-- |  19 | 张四   | 女     |        1 |
-- |  36 | 张 祁  | 女     |        3 |
......
-- 24 rows in set
-- 36、查询同名同姓学生名单，并统计同名人数；
select sname as '姓名' ,count(sname) as '同名人数'
from student group by sname having count(sname) >1;
-- +----------+----------+
-- | 姓名     | 同名人数 |
-- +----------+----------+
-- | 乔丹     |        2 |
-- | 何润婵   |        2 |
-- | 保罗     |        2 |
-- | 刘焕平   |        2 |
-- | 刘由材   |        4 |
-- | 刘翔     |        2 |
-- | 吉诺比利 |        2 |
-- ......
-- 63 rows in set
-- 37、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
select c.cid as '编号', c.cname as '课程', sc.avg_score as '平均分'
from course c ,
(select course_id, avg(score) as avg_score from score group by course_id) sc
where c.cid = sc.course_id
order by sc.avg_score asc ,c.cid desc ;
-- +------+------+---------+
-- | 编号 | 课程 | 平均分  |
-- +------+------+---------+
-- |    2 | 数学 | 68.0690 |
-- |    1 | 语文 | 68.1618 |
-- |    3 | 英语 | 68.6232 |
-- |    7 | 政治 | 74.2674 |
-- |    4 | 生物 | 74.4833 |
-- |    8 | 体育 | 74.5699 |
-- |    6 | 化学 | 75.1067 |
-- |    5 | 物理 | 75.3258 |
-- +------+------+---------+
-- 8 rows in set
-- 38、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
select s.sname as '姓名', sc.score as '分数' from student s
inner join
(select sc.student_id, sc.score from score sc
where sc.course_id = (select cid from course where cname='数学') and sc.score < 60) as sc
on s.sid = sc.student_id;
-- +----------+------+
-- | 姓名     | 分数 |
-- +----------+------+
-- | 韦德     |   40 |
-- | 吉诺比利 |   30 |
-- | 张三     |   38 |
-- ......
-- 73 rows in set
-- 39、查询课程编号为“3”且课程成绩在80分以上的学生的学号和姓名；
select s.sid as '学号', s.sname as '姓名' from student s
where s.sid in (select student_id from score where course_id = 3 and score >= 80);
-- +------+--------+
-- | 学号 | 姓名   |
-- +------+--------+
-- |    2 | 艾弗森 |
-- |    3 | 科比   |
-- |    6 | 麦迪   |
-- |    8 | 詹姆斯 |
-- |    9 | 韦德   |
-- ......
-- 73 rows in set
-- 40、求选修了课程的学生人数
select count(distinct(student_id)) as '选课人数' from score;
+----------+
| 选课人数 |
+----------+
|      277 |
+----------+
1 row in set
-- 41、查询选修“王五”老师所授课程的学生中，成绩最高和最低的学生姓名及其成绩；
 select s.sname, sc.* from student s  inner join
(select sc.student_id, sc.course_id, sc.score , sc1.max_score, sc1.min_score from score sc ,
(select course_id, max(score) as max_score ,min(score) as min_score from score sc
where sc.course_id in  (select cid from course where teacher_id=(select tid from teacher where tname='王五'))) as sc1
where sc1.course_id = sc.course_id and sc.score in (sc1.max_score, sc1.min_score)) as sc
on s.sid = sc.student_id;
-- +--------+------------+-----------+-------+-----------+-----------+
-- | sname  | student_id | course_id | score | max_score | min_score |
-- +--------+------------+-----------+-------+-----------+-----------+
-- | 李 丹  |        210 |         4 |    21 |       100 |        21 |
-- | 吴倩雯 |        214 |         4 |   100 |       100 |        21 |
-- | 齐同兴 |        234 |         4 |    21 |       100 |        21 |
-- | 吕 虎  |        238 |         4 |   100 |       100 |        21 |
-- | 朱顺忠 |        270 |         4 |    21 |       100 |        21 |
-- | 田 斌  |        274 |         4 |   100 |       100 |        21 |
-- +--------+------------+-----------+-------+-----------+-----------+
-- 6 rows in set
-- 42、查询各个课程及相应的选修人数；
 select sc.course_id as '编号', c.cname as '名称', count(sc.course_id) as '人数'
 from score sc, course c where c.cid = sc.course_id group by course_id;
--  +------+------+------+
-- | 编号 | 名称 | 人数 |
-- +------+------+------+
-- |    1 | 语文 |  168 |
-- |    2 | 数学 |  226 |
-- |    3 | 英语 |  216 |
-- |    4 | 生物 |   94 |
-- |    5 | 物理 |   92 |
-- |    7 | 政治 |  184 |
-- |    8 | 体育 |  183 |
-- +------+------+------+
-- 7 rows in set
-- 43、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
select s1.student_id, s1.course_id ,s1.score, s2.course_id, s2.score
from score s1, score s2
where s1.student_id = s2.student_id and s1.course_id != s2.course_id and s1.score = s2.score;
-- +------------+-----------+-------+-----------+-------+
-- | student_id | course_id | score | course_id | score |
-- +------------+-----------+-------+-----------+-------+
-- |         41 |         1 |    80 |         2 |    80 |
-- |        117 |         1 |    80 |         8 |    80 |
-- |        117 |         1 |    80 |         7 |    80 |
-- |        121 |         1 |    80 |         2 |    80 |
-- |        122 |         1 |    67 |         2 |    67 |
-- |        123 |         1 |    81 |         2 |    81 |
-- |        124 |         1 |    38 |         2 |    38 |
-- |        125 |         1 |    78 |         2 |    78 |
-- ......
-- 536 rows in set
-- 44、查询每门课程成绩最好的前两名学生id和姓名；
-- select c.cid as '编号', c.cname as '课程' ,
-- (select sc1.student_id from score sc1 where sc1.course_id = sc.course_id order by sc1.score desc limit 0,1) as '第一名学号',
-- (select s.sname from score sc1,student s  where sc1.course_id = sc.course_id and s.sid = sc1.student_id order by sc1.score desc limit 0,1) as '姓名',
-- (select sc1.student_id from score sc1 where sc1.course_id = sc.course_id order by sc1.score desc limit 1,1) as '第二名学号',
-- (select s.sname from score sc1,student s where sc1.course_id = sc.course_id and s.sid = sc1.student_id order by sc1.score desc limit 1,1) as '姓名'
-- from score sc , course c where c.cid = sc.course_id
-- group by sc.course_id;
-- +------+------+------------+--------+------------+--------+
-- | 编号 | 课程 | 第一名学号 | 姓名   | 第二名学号 | 姓名   |
-- +------+------+------------+--------+------------+--------+
-- |    1 | 语文 |         11 | 保罗   |        138 | 黄 江  |
-- |    2 | 数学 |          3 | 科比   |        156 | 汤维勇 |
-- |    3 | 英语 |          9 | 韦德   |        167 | 严建国 |
-- |    4 | 生物 |        214 | 吴倩雯 |        214 | 田 斌  |
-- |    5 | 物理 |         23 | 田 斌  |         23 | 李文辉 |
-- |    7 | 政治 |         82 | 段 凡  |        111 | 刘翔   |
-- |    8 | 体育 |         27 | 刘建东 |         54 | 段 凡  |
-- +------+------+------------+--------+------------+--------+
-- 7 rows in set
select c.cid as '编号', c.cname as '课程' ,
(select concat(sc1.student_id," : ",s.sname) from score sc1,student s  where sc1.course_id = sc.course_id and s.sid = sc1.student_id order by sc1.score desc limit 0,1) as '第一名',
(select concat(sc1.student_id," : ",s.sname) from score sc1,student s where sc1.course_id = sc.course_id and s.sid = sc1.student_id order by sc1.score desc limit 1,1) as '第二名'
from score sc , course c where c.cid = sc.course_id
group by sc.course_id;
-- +------+------+--------------+--------------+
-- | 编号 | 课程 | 第一名       | 第二名       |
-- +------+------+--------------+--------------+
-- |    1 | 语文 | 11 : 保罗    | 138 : 黄 江  |
-- |    2 | 数学 | 3 : 科比     | 156 : 汤维勇 |
-- |    3 | 英语 | 9 : 韦德     | 167 : 严建国 |
-- |    4 | 生物 | 214 : 吴倩雯 | 274 : 田 斌  |
-- |    5 | 物理 | 274 : 田 斌  | 50 : 李文辉  |
-- |    7 | 政治 | 82 : 段 凡   | 111 : 刘翔   |
-- |    8 | 体育 | 27 : 刘建东  | 54 : 段 凡   |
-- +------+------+--------------+--------------+
-- 45、检索至少选修两门课程的学生学号；
select student_id as '学号' from score group by student_id having count(student_id) >= 2;
-- +------------+
-- | student_id |
-- +------------+
-- |          1 |
-- |          2 |
-- |          3 |
-- |          4 |
-- |          5 |
-- |          6 |
-- ......
-- 277 rows in set
-- 46、查询没有学生选修的课程的课程号和课程名；
select cid as '课程号', cname as '课程' from course where cid not in (select distinct course_id from score);
-- +--------+------+
-- | 课程号 | 课程 |
-- +--------+------+
-- |      6 | 化学 |
-- +--------+------+
-- 1 row in set
-- 47、查询没带过任何班级的老师id和姓名；
select tid as '编号', tname as '姓名' from teacher where tid not in (select distinct tid from teacher2cls);
-- +------+------+
-- | 编号 | 姓名 |
-- +------+------+
-- |   11 | 远传 |
-- |   12 | egon |
-- +------+------+
-- 2 rows in set
-- 48、查询有两门以上课程超过80分的学生id及其平均成绩；
select sc.student_id as '学号', avg(sc.score) as '平均分' from score sc
where sc.student_id in (select student_id from score where score>80 group by student_id having count(student_id)>=2 )
group by student_id;
-- +------+---------+
-- | 学号 | 平均分  |
-- +------+---------+
-- |    2 | 71.5000 |
-- |    3 | 74.6000 |
-- |    6 | 70.0000 |
-- |    7 | 61.4000 |
-- |    8 | 80.0000 |
-- |    9 | 63.4000 |
-- ......
-- 29 rows in set
-- 49、检索“3”课程分数小于60，按分数降序排列的同学学号；
select student_id as '学号', score as '分数' from score where course_id=3 and score<60 order by score desc;
-- +------+------+
-- | 学号 | 分数 |
-- +------+------+
-- |    4 |   59 |
-- |  132 |   59 |
-- |   63 |   59 |
-- |  159 |   59 |
-- |  100 |   40 |
-- ......
-- 29 rows in set
-- 50、删除编号为“2”的同学的“1”课程的成绩；
delete from score where student_id = 2 and course_id = 1;
-- 51、查询同时选修了物理课和生物课的学生id和姓名；
select s.sid as '学号', s.sname as '姓名' from student s
where s.sid in
(select sc.student_id from score sc where sc.course_id in (select cid from course where cname in ('物理','生物'))
group by sc.student_id having count(sc.course_id)=2 );
-- +------+--------+
-- | 学号 | 姓名   |
-- +------+--------+
-- |  240 | 刘先承 |
-- |  241 | 彭 啟  |
-- |  242 | 袁 亮  |
-- |  243 | 贾天顺 |
-- |  244 | 何正良 |
-- |  245 | 黄 河  |
-- ......
-- 78 rows in set