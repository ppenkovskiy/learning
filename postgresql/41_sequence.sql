drop sequence if exists seq1;

create sequence seq1;

select nextval('seq1');
select currval('seq1');
select lastval();

select setval('seq1', 16, true);
select currval('seq1');
select nextval('seq1');

select setval('seq1', 16, false);
select currval('seq1');
select nextval('seq1');

create sequence if not exists seq2 increment 16;
select nextval('seq2');

drop sequence if exists seq3;

create sequence if not exists seq3
increment 16
minvalue 0
maxvalue 128
start with 0;

select nextval('seq3');

alter sequence seq3 rename to seq4;
alter sequence seq4 restart with 16;

select nextval('seq4');

drop sequence seq4;





