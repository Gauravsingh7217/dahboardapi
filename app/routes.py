from flask import Blueprint, jsonify
from .models import Distributor, Agent, Transaction

main = Blueprint('main', __name__)

@main.route('/api/business-stats')
def get_stats():
    total_distributors = Distributor.query.count()
    total_agents = Agent.query.count()
    active_agents = Agent.query.filter_by(status='active').count()
    non_active_agents = total_agents - active_agents
    total_business = sum(t.amount for t in Transaction.query.all())
    success_ratio = round((active_agents / total_agents) * 100) if total_agents else 0

    return jsonify({
        "total_business": total_business,
        "total_distributors": total_distributors,
        "total_agents": total_agents,
        "active_agents": active_agents,
        "non_active_agents": non_active_agents,
        "success_ratio": success_ratio
    })
