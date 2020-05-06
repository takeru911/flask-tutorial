BACKEND:=backend
FRONTEND:=frontend

# BACK

run-bachend:
	$(MAKE) -C $(BACNEND) run


# FRONT

run-frontend:
	$(MAKE) -C $(FRONTEND) run

build-frontend:
	$(MAKE) -C $(FRONTEND) build

