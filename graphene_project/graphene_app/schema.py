import graphene
import copy
from graphene_django.types import DjangoObjectType, ObjectType
from .models import CardBoard

class CardBoardType(DjangoObjectType):
    class Meta:
        model = CardBoard

class Query(ObjectType):
    label = graphene.Field(CardBoardType, id=graphene.ID())
    all_label = graphene.List(CardBoardType)
    
    def resolve_label(self, info, id=None):
        # label = kwargs.get('label')
        # if label is not None:
        #     return CardBoard.objects.get(label=label)
        
        # return None

        return CardBoard.objects.get(pk=id)


    def resolve_all_label(self, info, **kwargs):
        return CardBoard.objects.all()

###############################################################

class CardBoardInput(graphene.InputObjectType):
    label = graphene.String()
    date = graphene.Date()

class CreateCardBoard(graphene.Mutation):
    class Arguments:
        input = CardBoardInput(required=True)
    
    label = graphene.Field(CardBoardType)

    def mutate(root, info, input=None):
        label_instance = CardBoard(label=input.label)
        label_instance.save()
        return CreateCardBoard(label=label_instance)

################################################################

class UpdateCardBoardInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    label = graphene.String()
    date = graphene.Date()


class UpdateCardBoard(graphene.Mutation):
    labelQuery = graphene.Field(CardBoardType)

    class Arguments:
        input = UpdateCardBoardInput(required=True)

    def mutate(self, info, input):
        newLabel = CardBoard.objects.get(pk=input.id)
        
        if newLabel is not None:
            newLabel.label = input.label
            newLabel.save()
            return UpdateCardBoard(newLabel)
        
        return None


class DeleteCardBoard(graphene.Mutation):
    labelQuery = graphene.Field(CardBoardType)

    class Arguments:
        id = graphene.ID(required=True)
        
    def mutate(self, info, id):
        dCard = CardBoard.objects.get(pk=id)
        copy_dCard = copy.copy(dCard)
        if dCard is not None:
            dCard.delete()
            return DeleteCardBoard(copy_dCard)
        return None
        

################################################################

class Mutation(graphene.ObjectType):
    create_label = CreateCardBoard.Field()
    update_label = UpdateCardBoard.Field()
    delete_card = DeleteCardBoard.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)