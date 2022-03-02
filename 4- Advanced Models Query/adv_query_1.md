**1-Methods That Return QuerySets**\
_i will keeping updating these_

Method  | Description
------------- | -------------
**filter()**|Filter by the given lookup parameters. Multiple parameters are joined by SQL AND statements
**exclude()**|	Filter by objects that don’t match the given lookup parameters
**annotate()**|	Annotate each object in the QuerySet. Annotations can be simple values, a field reference or an aggregate expression
**order_by()**|	Change the default ordering of the QuerySet
**reverse()**|	Reverse the default ordering of the QuerySet
**distinct()**|	Perform an SQL SELECT DISTINCT query to eliminate duplicate rows
**values()**|	Returns dictionaries instead of model instances
**values_list()**|	Returns tuples instead of model instances
**dates()**|	Returns a QuerySet containing all available dates in the specified date range
**datetimes()**|	Returns a QuerySet containing all available dates in the specified date and time range
**none()**|	Create an empty QuerySet
**all()**|	Return a copy of the current QuerySet
**union()**|	Use the SQL UNION operator to combine two or more QuerySets
**intersection()**|	Use the SQL INTERSECT operator to return the shared elements of two or more QuerySets
**difference()**|	Use the SQL EXCEPT operator to return elements in the first QuerySet that are not in the others
**select_related()**|	Select all related data when executing the query (except many-to-many relationships)
**prefetch_related()**|	Select all related data when executing the query (including many-to-many relationships)
**defer()**|	Do not retrieve the named fields from the database. Used to improve query performance on complex datasets
**only()**|	Opposite of defer()—return only the named fields
**using()**|	Select which database the QuerySet will be evaluated against (when using multiple databases)
**select_for_update()**|	Return a QuerySet and lock table rows until the end of the transaction
**raw()**|	Execute a raw SQL statement
**AND (&)**|	Combine two QuerySets with the SQL AND operator. Using AND (&) is functionally equivalent to using filter() with multiple parameters
**OR (\|)**|	Combine two QuerySets with the SQL OR operator

**2- Methods That Don’t Return QuerySets**
Method  | Description
------------- | -------------
**get()**|	Returns a single object. Throws an error if lookup returns multiple objects
**create()**|	Shortcut method to create and save an object in one step
**get_or_create()**|	Returns a single object. If the object doesn’t exist, it creates one
**update_or_create()**|	Updates a single object. If the object doesn’t exist, it creates one
**bulk_create()**|	Insert a list of objects in the database
**bulk_update()**|	Update given fields in the listed model instances
**count()**|	Count the number of objects in the returned QuerySet. Returns an integer
**in_bulk()**|	Return a QuerySet containing all objects with the listed IDs
**iterator()**|	Evaluate a QuerySet and return an iterator over the results. Can improve performance and memory use for queries that return a large number of objects
**latest()**|	Return the latest object in the database table based on the given field(s)
**earliest()**|	Return the earliest object in the database table based on the given field(s)
**first()**|	Return the first object matched by the QuerySet
**last()**|	Return the last object matched by the QuerySet
aggregate()|	Return a dictionary of aggregate values calculated over the QuerySet
**exists()**|	Returns True if the QuerySet contains any results
**update()**|	Performs an SQL UPDATE on the specified field(s)
**delete()**|	Performs an SQL DELETE that deletes all rows in the QuerySet
**as_manager()**|	Return a Manager class instance containing a copy of the QuerySet’s methods
**explain()**|	Returns a string of the QuerySet’s execution plan. Used for analyzing query performance
