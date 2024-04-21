from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer

class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_RATE = 0.45
    
    def __init__(self, username: str, followers: int, engagement_rate: float) -> None:
        super().__init__(username, followers, engagement_rate)
        
    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget*self.INITIAL_PAYMENT_RATE
    
    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign" :
           return  int(self.followers * self.engagement_rate * 1.2)
       
        if campaign_type == "LowBudgetCampaign" :
            return  int(self.followers * self.engagement_rate * 0.9)
        
    def display_campaigns_participated(self):
        if self.campaigns_participated==[]:
            return f"{self.username} has not participated in any campaigns."
        
        campaign_messages = [f"  - Campaign ID: {c_p.campaign_id}, Brand: {c_p.brand}, Reached followers: {self.reached_followers(str(type(c_p)))}" for c_p in self.campaigns_participated]
        string = '\n'.join(campaign_messages)
        
        message =  f"{self.__class__.__name__} :) {self.username} :) participated in the following campaigns:\n{string}"
        return message  