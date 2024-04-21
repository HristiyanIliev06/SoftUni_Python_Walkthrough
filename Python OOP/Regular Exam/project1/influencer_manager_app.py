from typing import List
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign

from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer

class InfluencerManagerApp:
    INFLUENCER_TYPES = ['PremiumInfluencer', 'StandardInfluencer']
    CAMPAIGN_TYPES = ['HighBudgetCampaign', 'LowBudgetCampaign']
    REGISTERED_INFLUENCER_NAMES = []
    CREATED_CAMPAIGN_IDS = []
    
    
    def __init__(self) -> None:
        #self.influencers= []
        #self.campaigns = []
        self.influencers: List[PremiumInfluencer | StandardInfluencer] = []
        self.campaigns: List[HighBudgetCampaign | LowBudgetCampaign] = []
        
    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.INFLUENCER_TYPES: return f"{influencer_type} is not an allowed influencer type."
        if username in self.REGISTERED_INFLUENCER_NAMES: return f"{username} is already registered."
        
        self.REGISTERED_INFLUENCER_NAMES.append(username)
        influencer = PremiumInfluencer(username, followers, engagement_rate) if influencer_type=="PremiumInfluencer" else StandardInfluencer(username, followers, engagement_rate)
        self.influencers.append(influencer)
        
        return f"{username} is successfully registered as a {influencer_type}."
    
    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.CAMPAIGN_TYPES: return f"{campaign_type} is not a valid campaign type."
        if campaign_id in self.CREATED_CAMPAIGN_IDS: return f"Campaign ID {campaign_id} has already been created."
        
        self.CREATED_CAMPAIGN_IDS.append(campaign_id)
        campaign = HighBudgetCampaign(campaign_id, brand, required_engagement) if campaign_type=="HighBudgetCampaign" else LowBudgetCampaign(campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)
        
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."
    
    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        if influencer_username not in self.REGISTERED_INFLUENCER_NAMES:
            return f"Influencer '{influencer_username}' not found."
        
        if campaign_id not in self.CREATED_CAMPAIGN_IDS:
            return f"Campaign with ID {campaign_id} not found."
        
        our_influencer = self._get_influencer(influencer_username)
        our_campaign = self._get_campaign(campaign_id)
        if our_influencer!=None and our_campaign!= None:
                
            if our_campaign.check_eligibility(our_influencer.engagement_rate)!=True: 
                return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."
        
            if our_influencer.calculate_payment(type(our_campaign))>0.0:
                our_campaign.approved_influencers.append(our_influencer)
                our_campaign.budget-=our_influencer.calculate_payment(type(our_campaign))
                our_influencer.campaigns_participated.append(our_campaign)
                return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."
        
    def calculate_total_reached_followers(self):
        d = {}
        for inf in self.influencers:
            cp:List[HighBudgetCampaign | LowBudgetCampaign] = [item for item in inf.campaigns_participated]
            for item in cp: d[item] = inf.reached_followers(type(item))
            
        return dict(sorted(d.items(), key=lambda item: item[1]))
                
    def    
    
    def _get_campaign(self, campaign_id: str):
        our_campaigns = [c for c in self.campaigns if c.campaign_id == campaign_id]
        return our_campaigns[0] if our_campaigns else None

    def _get_influencer(self, username: str):
        our_influencers = [i for i in self.influencers if i.username == username]
        return our_influencers[0] if our_influencers else None
        
                    
            
        