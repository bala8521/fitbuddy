/**
 * FitBuddy Client Application Script
 */

document.addEventListener('DOMContentLoaded', () => {
  initDayTabs();
  initFormLoaders();
  initNutritionTipFetcher();
});

/**
 * Initializes tab switching for 7-day workout routine
 */
function initDayTabs() {
  const tabButtons = document.querySelectorAll('.day-tab-btn');
  const dayCards = document.querySelectorAll('.day-plan-card');

  if (!tabButtons.length || !dayCards.length) return;

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetDay = btn.getAttribute('data-day');

      // Update active tab button
      tabButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Show targeted day card
      dayCards.forEach(card => {
        if (card.getAttribute('data-day') === targetDay || targetDay === 'all') {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/**
 * Attaches loading state spinners to forms upon submission
 */
function initFormLoaders() {
  const forms = document.querySelectorAll('form[data-loading]');

  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      const submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        const originalText = submitBtn.innerHTML;
        const loadingText = form.getAttribute('data-loading-text') || 'Generating with Gemini AI...';
        submitBtn.innerHTML = `<span class="spinner"></span> ${loadingText}`;
      }
    });
  });
}

/**
 * Interactive quick nutrition / recovery tip fetcher
 */
function initNutritionTipFetcher() {
  const tipBtn = document.getElementById('fetch-quick-tip-btn');
  const tipContainer = document.getElementById('quick-tip-result');

  if (!tipBtn || !tipContainer) return;

  tipBtn.addEventListener('click', async () => {
    const goalSelect = document.getElementById('tip-goal-select');
    const goal = goalSelect ? goalSelect.value : 'General Wellness';

    tipBtn.disabled = true;
    tipBtn.innerHTML = `<span class="spinner"></span> Fetching Tip...`;
    tipContainer.innerHTML = `<div class="alert alert-info">Consulting FitBuddy Nutrition AI...</div>`;

    try {
      const response = await fetch('/api/nutrition/tip', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ goal: goal })
      });

      const data = await response.json();
      if (response.ok) {
        tipContainer.innerHTML = `
          <div class="alert alert-success">
            <strong>💡 ${data.goal} Tip:</strong>
            <p class="mt-1">${data.tip}</p>
          </div>
        `;
      } else {
        tipContainer.innerHTML = `
          <div class="alert alert-danger">
            ${data.detail || 'Could not fetch tip at this moment.'}
          </div>
        `;
      }
    } catch (err) {
      tipContainer.innerHTML = `
        <div class="alert alert-danger">
          Network connection issue while requesting nutrition tip.
        </div>
      `;
    } finally {
      tipBtn.disabled = false;
      tipBtn.innerHTML = `Get Nutrition Tip`;
    }
  });
}
