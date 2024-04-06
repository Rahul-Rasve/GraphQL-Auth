import graphene
import graphql_jwt
import api.schema

class Mutation(api.schema.Mutation, graphene.ObjectType):
    login = graphql_jwt.ObtainJSONWebToken.Field() #login user
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()    
    pass

# Query
class Query(api.schema.Query, graphene.ObjectType):
    pass

# Create schema
schema = graphene.Schema(query=Query, mutation=Mutation)