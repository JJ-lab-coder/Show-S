# Overview

This project is a REST API built for the KV5035 Software Architecture module.
It provides data about authors, presentations, and types from a conference database.

---

# Base URL:
https://w24016974.nuwebspace.co.uk/KV5035/api/

---

# Endpoints:
About

Returns basic information about the API.

GET /about.php

---

# Author :

Returns a list of authors.

GET /author.php

---

# Optional parameters:

author-id → get a specific author

presentation-id → get authors for a presentation

page → page number

size → number of results per page

---

# Examples
/author.php?author-id=21

/presentation.php?presentation-id=21

/author.php?page=1&size=10

---

# Presentation
Returns presentation data.

GET /presentation.php

---

# Optional parameters:
presentation-id → get a specific presentation

author-id → get presentations by an author

---

# Types

Handles presentation types.

GET /type.php

POST /type.php

PUT /type.php

PATCH /type.php

DELETE /type.php

---

# Tools
PHP

MySQL

JSON

