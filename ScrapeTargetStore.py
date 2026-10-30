class ScrapeTargetStore:
    def __init__(self, mongo_uri=None, db_name='social_scraper'):
        raise Exception('Forced mock mode')
    def add_target(self, platform, target_type, value, added_by='admin'):
        pass
    def get_active_targets(self, platform=None, target_type=None):
        return []
    def get_all_targets(self, platform=None):
        return []
    def mark_scraped(self, platform, target_type, value):
        pass
    def toggle_active(self, platform, target_type, value):
        pass
    def delete_target(self, platform, target_type, value):
        pass
    def deactivate_target(self, platform, target_type, value):
        pass
    def get_stats(self):
        return {'total': 0, 'active': 0, 'inactive': 0, 'by_platform': {}}