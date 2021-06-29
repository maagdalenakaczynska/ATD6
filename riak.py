import string
import riak

myClient = riak.RiakClient(pb_port=8087, protocol='pbc')

myBucket = myClient.bucket('ATD6')

person = {"name" : "Adam",
          "surname" : Krychowiak,
          "age": "n/a"
          "isMarried":"n/a"}

newPerson = myBucket.new(person['name'], data = person)
newPerson.store()
print("Zapisano, key: " + myBucket.key + " | data = " + str(myBucket.data))

fetched1 = myBucket.get(newPerson.key)
print("Pobrano, key: " + fetched1.key + " | data = " + str(fetched1.data))

fetched2 = fetched1.data
fetched2["age"] = "25"
fetched2["isMarried"] = "true"
fetched1 = fetched2
fetched1.store()

fetched1 = myBucket.get(newPerson.key)
print("Pobrano zaktualizowane, key: " + fetched1.key + " | data = " + str(fetched1.data))

myBucket.delete(fetched1.key)
print("Proba pobrania usunietego: " + fetched1.key + " | data = " + str(myBucket.get(fetched1).data))

