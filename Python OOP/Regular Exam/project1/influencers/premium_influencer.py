from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer

class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_RATE = 0.85
    
    
    def __init__(self, username: str, followers: int, engagement_rate: float) -> None:
        super().__init__(username, followers, engagement_rate)
        
    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget*self.INITIAL_PAYMENT_RATE
    
    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign" :
           return  int(self.followers * self.engagement_rate * 1.5)
       
        if campaign_type == "LowBudgetCampaign" :
            return  int(self.followers * self.engagement_rate * 0.8)
        
def display_campaigns_participated(self):
        if self.campaigns_participated==[]:
            return f"{self.username} has not participated in any campaigns."
        
        campaign_messages = [f"  - Campaign ID: {c_p.campaign_id}, Brand: {c_p.brand}, Reached followers: {self.reached_followers(str(type(c_p)))}" for c_p in self.campaigns_participated]
        string = '\n'.join(campaign_messages)
        
        message =  f"{self.__class__.__name__} :) {self.username} :) participated in the following campaigns:\n{string}"
        return message    
 
'''a = PremiumInfluencer("ffwjf", 34, 0.54)
b = HighBudgetCampaign(1, "fwf", 3.5)
a.campaigns_participated.append(b)
b.approved_influencers.append(a)'''
#print(a.display_campaigns_participated)      