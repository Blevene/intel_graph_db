from py2neo import neo4j, node, rel
# Define the DB connection
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

# Screw Indexes
# Lets just create JSON formatted objects and then insert them later
# Maybe store the returned objects in a list?

# Screw Indexes

def addHash(uuid, malhash, filename, family, confidence, source, source_type):
    return ({"uuid":uuid, "md5hash":malhash, "filename":filename, "description":family,"confidence":int(confidence), "source":source,
             "source_type":source_type})

def addIp(uuid, ip, asn, desc, source, source_type):
    return ({"uuid":uuid, "ip":ip, "asn":asn, "description":desc, "source":source, "source_type":source_type})

def addDomain(uuid, fqdn, uri, ip, desc, source, source_type):
    return ({"uuid":uuid, "domain":fqdn, "uri":uri, "ip":ip, "description":desc, "source":source, "source_type":source_type})

# Add some faux data

bad = addHash(str(uuid.uuid4()), "0018dc56a15c284c11b733c41f6dd40f", "radiator.html", "Redirector.OI", 5, "clean-mx", "OSINT")
bad2 = addIp(str(uuid.uuid4()), "193.109.247.227", "AS29076", "Redirector.OI", "clean-mx", "OSINT")
bad3 = addDomain(str(uuid.uuid4()), "narod.ru", "lovial.narod.ru/statyi/teplo/radiator.html", "193.109.247.227", "Redirector.OI", "clean-mx", "OSINT")

#[debug] print bad, bad2, bad3

# Clear the entire database, there is no confirmation and this cannot be undone, deal with it.
#[debug] graph_db.clear()

# Testing graph creation using a kind of ugly method
intel_test = graph_db.create(
    node(bad3),
    node(bad2),
    node(bad),
    rel(0, "butts", 1),
    rel(2, "butts", 0)
)

# Function to insert stuff into graph_db

def insert_into_db(node_1, node_2, relationship_verb):
    return graph_db.create(node(node_1), node(node_2), rel(0, relationship_verb, 1))
    
# Function test
insert_into_db(bad, bad2, "hurr")

# Expect 2 nodes to be created with the first entry -> relationship -> second entry
