# Hashtables 2

## Colisions and how to work with them

### Collisions

So, if our hashing function returns 3 for both "beige" and "chartreuse", what are we supposed to do? If we do nothing, an insertion of "chartreuse"’s hex code will overwrite the hex code that is stored for the key of "beige".

### Chaining

To mitigate this, you can also allow each slot to hold a reference to a collection (or chain) of items. That way, if both "beige" and "chartreuse" hash to index 3, they can both still be found there. Let’s use the same collection of integers we looked at before and see how inserting them in a hash table would look if we handled collisions with chaining.

The advantage of doing this versus linear probing is that, on average, each slot is likely to have very few items, so even when we take collisions into account search, insertion, and deletion operations are still quite efficient

### Performance

Once we take collisions into account with our hash tables, the performance implications are a bit different. Now, in the worst case, search, insertion, and deletion operations take linear time (O(n)) and are not constant. The worst case would be if every hash table entry were placed inside the linked list that was referenced by a single index.

However, the average case is still constant time (O(1)). So, if we handle collisions well and we have a hashing function that does an excellent job of spreading the data evenly across the hash table, hash tables are very performant data structures.

## Define Load factor

The performance of hash tables for search, insertion, and deletion is constant time (O(1)) in the average case. However, in the worst case, those same operations are done in linear time (O(n)). The more collisions that your hash table has, the less performant the hash table is. To avoid collisions, a proper hash function and maintaining a low load factor is crucial. What is a load factor?

### Load Factor

The load factor of a hash table is trivial to calculate. You take the number of items stored in the hash table divided by the number of slots

Hash tables use an array for storage, so the load factor would be the number of occupied slots divided by the length of the array. So, an array of length 10 with three items in it has a load factor of 0.3, and an array of length 20 with twenty items has a load factor of 1. If you use linear probing for collision resolution, then the maximum load factor is 1. If you use chaining for collision resolution, then the load factor can be greater than 1.

As the load factor of your hash table increases, so does the likelihood of a collision, which reduces the performance of your hash table. Therefore, you need to monitor the load factor and resize your hash table when the load factor gets too large. The general rule of thumb is to resize your hash table when your load factor is greater than 0.7. Also, when you resize, it is common to double the size of the hash table. When you resize the array, you need to re-insert all of the items into this new hash table. You cannot simply copy the old items into the new hash table. Each item has to be rerun through the hashing function because the hashing function takes into account the size of the hash table when determining the index that it returns.

You can see that resizing is an expensive operation, so you don’t want to resize too often. However, when we average it out, hash tables are constant time (O(1)) even with resizing.

The load factor can also be too small. If the hash table is too large for the data that it is storing, then memory is being wasted. So, in addition to resizing, when the load factor gets too high, you should also resize when the load factor gets too low.

One way to know when to resize your hash table is to compute the load factor whenever an item is inserted or deleted into the hash table. If the load factor is too high or too low, then you need to resize.
