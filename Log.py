#!/usr/bin/env python2.7
import psycopg2


def log_analysis(query, string):
    '''
    The function takes in two parameters, one is the query to be executed and
    the second one is the helper string for better formatted answer.
    The function executes the query and prints the result in a formatted way.
    '''
    # Connect to an existing database
    connect = psycopg2.connect("dbname=news")
    # Open a cursor to perform database operations
    cur = connect.cursor()
    # Execute a query
    cur.execute(query)
    results = cur.fetchall()
    for result in results:
            print "{}  --  {} {}".format(result[0], result[1], string)
    cur.close()
    connect.close()
    print
    return

# First Query
print "1. What are the most popular three articles of all time?"
first_query = """
                SELECT title, count(*) AS views
                FROM articles JOIN log ON
                log.path LIKE concat('%',articles.slug,'%')
                WHERE log.status = '200 OK'
                GROUP BY title
                ORDER BY views DESC LIMIT 3;
              """
log_analysis(first_query, "views")

# Second Query
print "2. Who are the most popular authors of all time?"
second_query = """
                SELECT name, COUNT(*) AS views
                FROM authors JOIN articles ON
                authors.id = articles.author
                JOIN log ON articles.slug = SUBSTR(log.path,10)
                group by name
                order by views desc;
               """
log_analysis(second_query, "views")

# Third Query
print "3. On which days did more than 1% of requests lead to errors?"
third_query = """
                WITH answer AS (
                               SELECT CAST(time AS DATE) AS date,
                               round(100.0*sum(case status
                                               when '404 NOT FOUND' then 1
                                               else 0
                                               end)/count(status),1)
                                as per_fail
                                from log group by date
                               )
                SELECT to_char(date, 'FMMonth FMDD, YYYY'), per_fail
                FROM answer
                WHERE per_fail>1;
              """
log_analysis(third_query, "%")
