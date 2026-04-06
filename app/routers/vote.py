from .. import schemas,models, oauth2
from fastapi import Response,status,HTTPException,Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List,Optional

router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote : schemas.vote ,db : Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")

    vote_query = db.query(models.Votes).filter(models.Votes.posts_id == vote.post_id, models.Votes.user_id == current_user.id)
    found_vote = vote_query.first()
    
    if (vote.dir == 1) :
        if found_vote:
           raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User already liked this post")
        new_vote = models.Votes(posts_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return{"message" : "succesful vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="vote does not exist")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        return{"message" : "Deleted Succesfully"}
